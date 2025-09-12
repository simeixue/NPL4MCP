#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_tools_and_sources.py
- 连接多个 MCP server，list_tools
- 按 serverKey 找到对应源码仓库，解析工具实现
- 输出 ./results/tools_list_implementation.json ，每条包含 "server": serverKey
"""
import asyncio
import json
import os
import re
import sys
from typing import Dict, List, Optional
from utils.config_auto import REPO_BASE, SERVER_REPO_DIR, CONFIG, OUT_JSON, OUT_DIR

from fastmcp import Client


import sys
MAX_JS_DEPTH=3 # 深度
DEBUG = "--debug" in sys.argv

def dprint(*args, **kwargs):
    """只在 DEBUG 开启时打印"""
    if DEBUG:
        print(*args, **kwargs)

# ---------- 符号索引 ----------
import ast, os
from typing import Dict, Tuple, Set, Optional

def _is_py(path: str) -> bool:
    return path.endswith(".py") and not os.path.basename(path).startswith(".")

def _module_name(repo_root: str, file_path: str) -> str:
    rel = os.path.relpath(file_path, repo_root)
    rel = rel.replace(os.sep, "/")
    if rel.endswith(".py"):
        rel = rel[:-3]
    parts = [p for p in rel.split("/") if p and p != "__init__"]
    return ".".join(parts)

def build_repo_symbol_index(repo_root: str):
    """
    返回:
      modules: {module_name: file_path}
      file_funcs: {file_path: {func_name: ast.FunctionDef}}
      unique_name_index: {func_name: file_path}  # 仅唯一名
    """
    modules: Dict[str, str] = {}
    file_funcs: Dict[str, Dict[str, ast.AST]] = {}
    name_occurs: Dict[str, Set[str]] = {}

    for dirpath, _, filenames in os.walk(repo_root):
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            if not _is_py(path):
                continue
            mod = _module_name(repo_root, path)
            modules[mod] = path
            try:
                with open(path, "r", encoding="utf-8") as f:
                    src = f.read()
                tree = ast.parse(src, filename=path)
            except Exception:
                continue
            fdict: Dict[str, ast.AST] = {}
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    fdict[node.name] = node
                    name_occurs.setdefault(node.name, set()).add(path)
            file_funcs[path] = fdict

    unique_name_index: Dict[str, str] = {}
    for name, paths in name_occurs.items():
        if len(paths) == 1:
            unique_name_index[name] = next(iter(paths))

    return modules, file_funcs, unique_name_index


# -------------------------------------------------
# 提取函数：Python 匹配 @tool / @tool() / @mcp.tool / @mcp.tool()
# ---------- 跨文件提取 ----------
def _import_map_for_file(repo_root: str, file_path: str, modules: Dict[str, str]) -> Dict[str, str]:
    """
    返回 alias -> file_path，仅映射到本仓模块。
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            src = f.read()
        tree = ast.parse(src, filename=file_path)
    except Exception:
        return {}

    amap: Dict[str, str] = {}
    for n in tree.body:
        # import pkg.mod as alias
        if isinstance(n, ast.Import):
            for alias in n.names:
                mod = alias.name
                asname = alias.asname or mod.split(".")[0]
                if mod in modules:
                    amap[asname] = modules[mod]
        # from pkg.mod import foo as bar
        elif isinstance(n, ast.ImportFrom):
            if n.level and n.module is None:
                # 相对导入，构造模块名
                base = _module_name(repo_root, file_path).split(".")
                pkg = ".".join(base[:max(0, len(base)-n.level)])
                mod = f"{pkg}.{n.module}" if n.module else pkg
            else:
                mod = n.module or ""
            if mod in modules:
                target_path = modules[mod]
                for alias in n.names:
                    asname = alias.asname or alias.name
                    # 把符号名当作“模块别名”映射到该文件
                    # 用于识别 mod.func 以及直接 foo(...)（来自 from ... import foo）
                    amap[asname] = target_path
    return amap

def py_extract_from_file_with_repo(path: str, repo_root: str,
                                   modules=None, file_funcs=None, unique_name_index=None) -> Dict[str, str]:
    """
    提取 @mcp.tool，并递归展开依赖：
      - Name 调用：优先同文件；否则唯一名索引
      - Attribute 调用：仅当 obj 是 import 的本仓模块别名时，跳到该模块文件查找
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        tree = ast.parse(src, filename=path)
    except Exception:
        return {}

    if modules is None or file_funcs is None or unique_name_index is None:
        modules, file_funcs, unique_name_index = build_repo_symbol_index(repo_root)

    import_map = _import_map_for_file(repo_root, path, modules)
    this_funcs = file_funcs.get(path, {})
    expanded_cache: Dict[Tuple[str, str], str] = {}

    def _source_segment(fpath: str, node: ast.AST) -> str:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                s = f.read()
            return (ast.get_source_segment(s, node) or "").strip()
        except Exception:
            return ""

    def expand(fpath: str, fname: str, visited: Set[Tuple[str, str]], depth: int = 0) -> str:
        key = (fpath, fname)
        if key in expanded_cache:
            return expanded_cache[key]
        if key in visited:
            return f"# [Cyclic dependency detected: {fname} in {fpath}]"
        if depth > MAX_JS_DEPTH:
            return f"# [Max expansion depth reached at {fname}]"

        fdefs = file_funcs.get(fpath, {})
        node = fdefs.get(fname)
        if not node:
            return f"# [Function {fname} not found in {fpath}]"

        visited.add(key)
        parts = [_source_segment(fpath, node)]

        # 收集调用
        called: Set[Tuple[str, Optional[str]]] = set()  # (func_name, target_file or None)
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call):
                # foo(...)
                if isinstance(sub.func, ast.Name):
                    name = sub.func.id
                    # 当前文件优先
                    if name in fdefs:
                        called.add((name, fpath))
                    elif name in this_funcs and fpath == path:
                        called.add((name, path))
                    # 再用唯一名索引
                    elif name in unique_name_index:
                        called.add((name, unique_name_index[name]))
                # mod.func(...)
                elif isinstance(sub.func, ast.Attribute) and isinstance(sub.func.value, ast.Name):
                    mod_alias = sub.func.value.id
                    target_mod_file = import_map.get(mod_alias)
                    if target_mod_file:
                        called.add((sub.func.attr, target_mod_file))
                # 其余情况忽略（obj.method、第三方库等）

        # 递归展开
        for cname, tf in sorted(called):
            dep_src = expand(tf, cname, visited, depth + 1)
            if dep_src:
                parts.append(f"\n\n# Dependency: {cname} (from {tf})\n{dep_src}")

        visited.remove(key)
        code = "\n\n".join([p for p in parts if p])
        expanded_cache[key] = code
        return code

    results = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in n.decorator_list:
                if (
                    (isinstance(dec, ast.Name) and dec.id == "tool")
                    or (isinstance(dec, ast.Attribute) and dec.attr == "tool")
                    or (isinstance(dec, ast.Call) and (
                        (isinstance(dec.func, ast.Name) and dec.func.id == "tool") or
                        (isinstance(dec.func, ast.Attribute) and dec.func.attr == "tool")
                    ))
                ):
                    impl = expand(path, n.name, set(), 0)
                    results[n.name] = impl
    return results



# ---------- root 调用 ----------
def py_extract_from_root(root: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    modules, file_funcs, unique_name_index = build_repo_symbol_index(root)
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if _is_py(os.path.join(dirpath, fn)):
                p = os.path.join(dirpath, fn)
                tools = py_extract_from_file_with_repo(
                    p, root,
                    modules=modules,
                    file_funcs=file_funcs,
                    unique_name_index=unique_name_index
                )
                if tools and DEBUG:
                    dprint(f"[PY] {p} -> {list(tools.keys())}")
                out.update(tools)
    return out


# ================= TS/JS 递归提取（同文件 + 跨文件） =================
import os, re
from typing import Dict, List, Optional, Set, Tuple

MAX_JS_DEPTH = 64

def read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

def _match_balanced(s: str, start: int, open_ch="(", close_ch=")") -> int:
    stack = []
    i, L = start, len(s)
    in_s, quote = False, ""
    in_sl, in_ml = False, False
    while i < L:
        c = s[i]
        p = s[i-1] if i > 0 else ""
        # 注释
        if not in_s:
            if not in_ml and not in_sl and c == "/" and i+1 < L and s[i+1] == "/":
                in_sl = True; i += 2; continue
            if not in_ml and not in_sl and c == "/" and i+1 < L and s[i+1] == "*":
                in_ml = True; i += 2; continue
            if in_sl and c in "\r\n": in_sl = False
            if in_ml and c == "*" and i+1 < L and s[i+1] == "/":
                in_ml = False; i += 2; continue
            if in_sl or in_ml: i += 1; continue
        # 字符串/模板
        if not in_s and c in ("'", '"', "`"):
            in_s, quote = True, c; i += 1; continue
        if in_s:
            if quote == "`" and c == "$" and i+1 < L and s[i+1] == "{":
                j = _match_balanced(s, i+1, "{", "}")
                if j < 0: return -1
                i = j + 1; continue
            if c == quote and p != "\\": in_s = False; quote = ""
            i += 1; continue
        # 括号配对
        if c == open_ch: stack.append(c)
        elif c == close_ch:
            if stack:
                stack.pop()
                if not stack: return i
        i += 1
    return -1

def _split_top_args(s: str) -> List[str]:
    parts, last = [], 0
    depth = {"(": 0, "{": 0, "[": 0}
    in_s, quote, in_sl, in_ml = False, "", False, False
    i, L = 0, len(s)
    while i < L:
        c = s[i]
        p = s[i-1] if i > 0 else ""
        if not in_s:
            if not in_ml and not in_sl and c == "/" and i+1 < L and s[i+1] == "/":
                in_sl = True; i += 2; continue
            if not in_ml and not in_sl and c == "/" and i+1 < L and s[i+1] == "*":
                in_ml = True; i += 2; continue
            if in_sl and c in "\r\n": in_sl = False
            if in_ml and c == "*" and i+1 < L and s[i+1] == "/":
                in_ml = False; i += 2; continue
            if in_sl or in_ml: i += 1; continue
        if not in_s and c in ("'", '"', "`"):
            in_s, quote = True, c; i += 1; continue
        if in_s:
            if quote == "`" and c == "$" and i+1 < L and s[i+1] == "{":
                j = _match_balanced(s, i+1, "{", "}")
                if j < 0: return parts
                i = j + 1; continue
            if c == quote and p != "\\":
                in_s, quote = False, ""
            i += 1; continue
        if c in "({[": depth[c] += 1
        elif c in ")}]":
            opener = {")":"(", "}":"{", "]":"["}[c]
            depth[opener] -= 1
        if c == "," and all(v == 0 for v in depth.values()):
            parts.append(s[last:i].strip()); last = i + 1
        i += 1
    tail = s[last:].strip()
    if tail: parts.append(tail)
    return parts

def _is_inline_func(arg: str) -> bool:
    a = arg.strip()
    return a.startswith("function") or "=>" in a

def _slice_func(text: str, start: int) -> Optional[str]:
    arrow_idx = text.find("=>", start)
    if arrow_idx >= 0:
        j = arrow_idx + 2
        while j < len(text) and text[j].isspace(): j += 1
        if j < len(text) and text[j] == "{":
            end = _match_balanced(text, j, "{", "}")
            return text[start:end+1] if end >= 0 else None
        m = re.search(r'[;\n]', text[j:])
        k = j + (m.start() if m else len(text) - j)
        return text[start:k]
    brace_idx = text.find("{", start)
    if brace_idx >= 0:
        end = _match_balanced(text, brace_idx, "{", "}")
        return text[start:end+1] if end >= 0 else None
    return None

# ---------- JS/TS 仓库索引 ----------
def _is_js(path: str) -> bool:
    return path.endswith((".js", ".ts", ".mjs", ".cjs")) and not os.path.basename(path).startswith(".")

def _module_path_from_import(import_str: str, cur_file: str, repo_root: str) -> Optional[str]:
    """
    解析 import 源，支持:
      import x from './a/b'
      import {y} from '../c'
      const m = require('./d')
    仅解析相对路径到 repo 内部文件；忽略包名。
    """
    src = import_str.strip().strip('"\'')
    if src.startswith("."):
        base = os.path.dirname(cur_file)
        cand = os.path.normpath(os.path.join(base, src))
        # 加扩展或目录索引
        for ext in (".ts",".js",".mjs",".cjs"):
            if os.path.isfile(cand+ext): return cand+ext
        for idx in ("index.ts","index.js","index.mjs","index.cjs"):
            if os.path.isfile(os.path.join(cand, idx)): return os.path.join(cand, idx)
    return None

def _collect_named_functions(text: str) -> Dict[str, Tuple[int,int]]:
    """
    返回 {funcName: (start_idx, end_idx_inclusive)}
    支持:
      function foo(...) { ... }
      async function foo(...) { ... }
      const foo = (...) => { ... }
      export const foo = ... => { ... }
    """
    res: Dict[str, Tuple[int,int]] = {}

    for m in re.finditer(r'\b(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(', text):
        name = m.group(1)
        body = _slice_func(text, m.start())
        if body:
            res[name] = (m.start(), m.start() + len(body))

    for m in re.finditer(r'\b(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>', text, re.S):
        name = m.group(1)
        body = _slice_func(text, m.start())
        if body:
            res[name] = (m.start(), m.start() + len(body))

    return res

def build_js_repo_index(repo_root: str):
    """
    返回:
      file_text: {file_path: text}
      file_funcs: {file_path: {func_name: (start,end)}}
      import_graph: {file_path: {alias_or_spec: imported_file_path}}
    """
    file_text: Dict[str, str] = {}
    file_funcs: Dict[str, Dict[str, Tuple[int,int]]] = {}
    import_graph: Dict[str, Dict[str, str]] = {}

    for dirpath, _, filenames in os.walk(repo_root):
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            if not _is_js(path):
                continue
            text = read_text(path)
            file_text[path] = text
            file_funcs[path] = _collect_named_functions(text)

            imap: Dict[str, str] = {}
            # ES imports
            for m in re.finditer(r'^\s*import\s+([^;]+?)\s+from\s+([\'"][^\'"]+[\'"]);?', text, re.M):
                spec, src = m.group(1), m.group(2)
                target = _module_path_from_import(src, path, repo_root)
                if not target: continue
                # import foo from './x'
                mdef = re.match(r'^\s*([A-Za-z_$][\w$]*)\s*(,|\s*$)', spec.strip())
                if mdef:
                    imap[mdef.group(1)] = target
                # import * as ns from './x'
                mns = re.search(r'\*\s+as\s+([A-Za-z_$][\w$]*)', spec)
                if mns:
                    imap[mns.group(1)] = target
                # import {a as b, c} from ...
                for ms in re.finditer(r'([A-Za-z_$][\w$]*)(?:\s+as\s+([A-Za-z_$][\w$]*))?', spec):
                    orig, alias = ms.group(1), ms.group(2) or ms.group(1)
                    # 排除前面的默认和 namespace 已处理位置可能重复
                    imap[alias] = target
            # CommonJS require
            for m in re.finditer(r'^\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*require\(\s*([\'"][^\'"]+[\'"])\s*\)', text, re.M):
                alias, src = m.group(1), m.group(2)
                target = _module_path_from_import(src, path, repo_root)
                if target:
                    imap[alias] = target

            import_graph[path] = imap

    return file_text, file_funcs, import_graph

def _text_slice(text: str, span: Tuple[int,int]) -> str:
    s, e = span
    return text[s:e]

def _find_calls_simple(body: str) -> Set[Tuple[str, Optional[str]]]:
    """
    只识别两类调用：
      1) foo(    -> ('foo', None)
      2) mod.func(  -> ('func', 'mod')
    避免把 obj.method 当作库函数，保守处理。
    """
    called: Set[Tuple[str, Optional[str]]] = set()
    # mod.func(
    for m in re.finditer(r'\b([A-Za-z_$][\w$]*)\s*\.\s*([A-Za-z_$][\w$]*)\s*\(', body):
        called.add((m.group(2), m.group(1)))
    # foo(
    for m in re.finditer(r'(?<!\.)\b([A-Za-z_$][\w$]*)\s*\(', body):
        called.add((m.group(1), None))
    # 排除常见内置/关键词
    blacklist = {'if','for','while','switch','return','function','async','await','catch','then','map','filter','reduce','forEach','push','pop','slice','splice','JSON','parse','stringify','log','error'}
    called = {(f,mod) for (f,mod) in called if f not in blacklist}
    return called

def _expand_js_function(repo_root: str,
                        entry_file: str,
                        file_text: Dict[str,str],
                        file_funcs: Dict[str, Dict[str,Tuple[int,int]]],
                        import_graph: Dict[str, Dict[str,str]],
                        fname: str,
                        visited: Set[Tuple[str,str]],
                        depth: int = 0) -> str:
    key = (entry_file, fname)
    if key in visited:
        return f"// [Cyclic dependency detected: {fname} in {entry_file}]"
    if depth > MAX_JS_DEPTH:
        return f"// [Max expansion depth reached at {fname}]"

    funcs = file_funcs.get(entry_file, {})
    if fname not in funcs:
        return f"// [Function {fname} not found in {entry_file}]"
    text = file_text.get(entry_file, "")
    span = funcs[fname]
    src = _text_slice(text, span).strip()

    visited.add(key)
    parts = [src]

    body = src  # 粗略用全文片段查调用
    calls = _find_calls_simple(body)

    for callee, mod in sorted(calls):
        target_file = None
        if mod:
            # 仅当 mod 是 import 别名才追
            target_file = import_graph.get(entry_file, {}).get(mod)
        else:
            # 无模块前缀时，先在本文件找
            if callee in funcs:
                target_file = entry_file
            else:
                target_file = None  # 不做全局唯一名匹配，避免误报

        if target_file and callee in file_funcs.get(target_file, {}):
            dep = _expand_js_function(repo_root, target_file, file_text, file_funcs, import_graph, callee, visited, depth+1)
            if dep:
                parts.append(f"\n\n// Dependency: {callee} (from {target_file})\n{dep}")

    visited.remove(key)
    return "\n\n".join(parts)

# ---------- 入口提取 ----------
def _extract_server_tool_calls(text: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    i = 0
    while True:
        start = text.find("server.tool(", i)
        if start < 0: break
        paren_open = start + len("server.tool")
        end = _match_balanced(text, paren_open, "(", ")")
        if end < 0:
            i = start + 1
            continue
        args_text = text[paren_open+1:end]
        args = _split_top_args(args_text)
        if len(args) >= 2:
            m_name = re.match(r"""['"]([^'"]+)['"]""", args[0].strip())
            if m_name:
                tool = m_name.group(1)
                handler_arg = args[-1].strip()
                if _is_inline_func(handler_arg):
                    seg = text[paren_open+1:end]
                    mm = re.search(r'(?:async\s+)?\([^)]*\)\s*=>\s*\{|(?:async\s+)?function\s*\([^)]*\)\s*\{', seg, re.S)
                    if mm:
                        pos = (paren_open+1)+mm.start()
                        impl = _slice_func(text, pos)
                    else:
                        impl = None
                else:
                    m_ident = re.match(r'([A-Za-z_$][\w$]*)', handler_arg)
                    impl = (tool, m_ident.group(1)) if m_ident else None  # 返回占位，后续用命名函数展开
                if impl:
                    out[tool] = impl
        i = end + 1
    return out  # 值可能是字符串(内联源码) 或 元组(tool, handlerName)

def _extract_switch_handlers(text: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for sw in re.finditer(r'switch\s*\(\s*request\.params\.name\s*\)\s*\{', text):
        sw_open = sw.end()-1
        sw_close = _match_balanced(text, sw_open, "{", "}")
        if sw_close < 0: continue
        body = text[sw_open+1:sw_close]
        for cm in re.finditer(r'case\s+["\']([^"\']+)["\']\s*:\s*', body):
            tool = cm.group(1)
            seg_start = cm.end()
            next_m = re.search(r'\bcase\s+["\']|default\s*:', body[seg_start:])
            seg_end = seg_start + (next_m.start() if next_m else len(body[seg_start:]))
            segment = body[seg_start:seg_end]
            call = re.search(r'\breturn\s+(?:await\s+)?([A-Za-z_$][\w$]*)\s*\(', segment)
            if call:
                out[tool] = ("_BY_NAME_", call.group(1))
    return out  # 值为 ("_BY_NAME_", handlerName)

def js_extract_from_file_with_repo(path: str, repo_root: str,
                                   file_text: Dict[str,str],
                                   file_funcs: Dict[str, Dict[str,Tuple[int,int]]],
                                   import_graph: Dict[str, Dict[str,str]]) -> Dict[str, str]:
    text = file_text.get(path) or read_text(path)
    out: Dict[str, str] = {}

    # 1) server.tool(...)
    tools = _extract_server_tool_calls(text)
    for tool, impl in tools.items():
        if isinstance(impl, str):
            # 内联函数，直接作为入口，再递归把子函数加进来（从当前文件名函数无法命名，递归不到）
            out[tool] = impl.strip()
        else:
            # 命名处理器
            _tag, handler = impl
            if handler in file_funcs.get(path, {}):
                code = _expand_js_function(repo_root, path, file_text, file_funcs, import_graph, handler, set(), 0)
                out[tool] = code.strip()

    # 2) 分发器 switch(request.params.name)
    sw = _extract_switch_handlers(text)
    for tool, tpl in sw.items():
        _tag, handler = tpl
        # 在当前文件或通过 import 的模块中寻找 handler
        code = None
        if handler in file_funcs.get(path, {}):
            code = _expand_js_function(repo_root, path, file_text, file_funcs, import_graph, handler, set(), 0)
        else:
            # 尝试在 import 的别名模块里找同名函数
            for alias, tfile in import_graph.get(path, {}).items():
                if handler in file_funcs.get(tfile, {}):
                    code = _expand_js_function(repo_root, tfile, file_text, file_funcs, import_graph, handler, set(), 0)
                    break
        if code:
            out.setdefault(tool, code.strip())

    return out

def js_extract_from_root(root: str) -> Dict[str, str]:
    file_text, file_funcs, import_graph = build_js_repo_index(root)
    out: Dict[str, str] = {}
    for f in list(file_text.keys()):
        tools = js_extract_from_file_with_repo(f, root, file_text, file_funcs, import_graph)
        if tools and DEBUG:
            dprint(f"[JS/TS] {f} -> {list(tools.keys())}")
        out.update(tools)
    return out

# ================= 索引并汇总 =================

def build_source_index() -> Dict[str, Dict[str, str]]:
    idx: Dict[str, Dict[str, str]] = {}
    for srv, folder in SERVER_REPO_DIR.items():
        root = os.path.join(REPO_BASE, folder)
        if not os.path.isdir(root):
            dprint(f"[WARN] repo not found for {srv}: {root}")
            continue
        py_map = py_extract_from_root(root)
        js_map = js_extract_from_root(root)
        merged = dict(js_map)
        merged.update(py_map)
        if DEBUG:
            dprint(f"[INDEX] server={srv}, tools={list(merged.keys())}")
        idx[srv] = merged
    return idx

async def list_and_collect() -> List[dict]:
    """Per-server listing. 每个 tool 明确标注它所属的 server。"""
    os.makedirs(OUT_DIR, exist_ok=True)

    # 源码索引：{server_key: {tool_name: implementation}}
    src_idx = build_source_index()
    server_keys = list(CONFIG.get("mcpServers", {}).keys())

    def _norm(s: str) -> str:
        return re.sub(r'[^a-z0-9_]+', '', s.lower())

    results: List[dict] = []

    # 逐个 server 启动并仅匹配该 server 的源码
    for srv in server_keys:
        srv_cfg = {"mcpServers": {srv: CONFIG["mcpServers"][srv]}}
        mapping = src_idx.get(srv, {})
        nmap = {_norm(k): (k, v) for k, v in mapping.items()}

        client = Client(srv_cfg)
        async with client:
            tools = await client.list_tools()
            for t in tools:
                impl = "<source code unavailable>"

                # 1) 精确匹配（当前 server 下）
                if t.name in mapping:
                    impl = mapping[t.name]
                else:
                    # 2) 规范化匹配
                    tnorm = _norm(t.name)
                    if tnorm in nmap:
                        impl = nmap[tnorm][1]
                    else:
                        # 3) 去掉当前 server 前缀再匹配
                        prefix = srv.lower() + "_"
                        stripped = t.name[len(srv)+1:] if t.name.lower().startswith(prefix) else t.name
                        if stripped in mapping:
                            impl = mapping[stripped]
                        else:
                            snorm = _norm(stripped)
                            if snorm in nmap:
                                impl = nmap[snorm][1]

                results.append({
                    "server": srv,               # 明确标注 tool 属于哪个 server
                    "name": t.name,              # 保留 MCP 返回的原始名字，不改动
                    "description": t.description,
                    "implementation": impl,
                    "input_schema": getattr(t, "inputSchema", None),
                    "annotations": getattr(t, "annotations", None),
                })

    return results


def main():
    if DEBUG:
        dprint("=== DEBUG MODE ENABLED ===")

    data = asyncio.run(list_and_collect())
    os.makedirs(os.path.dirname(OUT_JSON) or ".", exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Wrote", OUT_JSON, f"({len(data)} tools)")

if __name__ == "__main__":
    main()