#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, ast, json, csv
from typing import Dict, List, Tuple, Optional

SKIP_DIRS = {".git", ".hg", ".svn", "__pycache__", ".mypy_cache", ".pytest_cache", "venv", ".venv", "env"}

class FuncDef:
    def __init__(self, fqn: str, file: str, start: int, end: int, code: str):
        self.fqn = fqn
        self.file = file
        self.start = start
        self.end = end
        self.code = code

def rel_module_name(root: str, file_path: str) -> str:
    rel = os.path.relpath(file_path, root)
    rel = rel.replace(os.sep, "/")
    if rel.endswith(".py"):
        rel = rel[:-3]
    if rel.endswith("/__init__"):
        rel = rel[: -len("/__init__")]
    parts = [p for p in rel.split("/") if p]
    return ".".join(parts) if parts else os.path.basename(root)

def read_text(fp: str) -> str:
    with open(fp, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def find_py_files(root: str) -> List[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            if fn.endswith(".py"):
                out.append(os.path.join(dirpath, fn))
    return out

class Indexer(ast.NodeVisitor):
    """
    第一遍：收集函数定义，建立索引
    生成：
      - func_defs: fqn -> FuncDef
      - module_index: module -> set(simple_name)
      - class_index: (module, class) -> set(method_name)
    """
    def __init__(self, root: str, file: str, module: str, src: str):
        self.root = root
        self.file = file
        self.module = module
        self.src = src.splitlines()
        self.func_defs: Dict[str, FuncDef] = {}
        self.module_index: Dict[str, set] = {module: set()}
        self.class_index: Dict[Tuple[str, str], set] = {}
        self.scope_stack: List[str] = []  # class / function names for FQN

    def _node_code(self, node: ast.AST) -> Tuple[int, int, str]:
        start = getattr(node, "lineno", None)
        end = getattr(node, "end_lineno", None)
        if start is None or end is None:
            # 退路：粗略匹配到下一定义前
            end = start
            while end < len(self.src) and self.src[end-1].strip() != "":
                end += 1
        code = "\n".join(self.src[start-1:end])
        return start, end, code

    def _fqn(self, name: str) -> str:
        parts = [self.module] + self.scope_stack + [name]
        return ".".join([p for p in parts if p])

    def visit_ClassDef(self, node: ast.ClassDef):
        self.scope_stack.append(node.name)
        self.class_index.setdefault((self.module, node.name), set())
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        start, end, code = self._node_code(node)
        fqn = self._fqn(node.name)
        self.func_defs[fqn] = FuncDef(fqn, self.file, start, end, code)
        # 记录到模块或类索引
        if len(self.scope_stack) >= 1 and isinstance(self.scope_stack[-1], str):
            # 若栈顶是类名，则记为方法
            cls = self.scope_stack[-1]
            # 粗判：如果上一层是类（无法从栈直接知道），用是否在 class_index 中判断
            if (self.module, cls) in self.class_index:
                self.class_index[(self.module, cls)].add(node.name)
            else:
                self.module_index[self.module].add(node.name)
        else:
            self.module_index[self.module].add(node.name)

        # 支持嵌套函数：入栈后继续
        self.scope_stack.append(node.name)
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.visit_FunctionDef(node)

class CallCollector(ast.NodeVisitor):
    """
    第二遍：收集调用边（仅解析到本仓库中有定义的目标）
    只在函数体内记录边： current_fqn -> callee_fqn
    支持模式：
      - foo()                 -> 同模块函数
      - self.foo()            -> 当前类的方法
      - ClassName.foo()       -> 模块内类的方法
    """
    def __init__(self, module: str, file: str, index_all_funcs: Dict[str, FuncDef],
                 module_index: Dict[str, set], class_index: Dict[Tuple[str, str], set]):
        self.module = module
        self.file = file
        self.index_all_funcs = index_all_funcs
        self.module_index = module_index
        self.class_index = class_index
        self.current_func_stack: List[str] = []
        self.current_class_stack: List[str] = []
        self.edges: List[Tuple[str, str, int]] = []  # caller, callee, call_line

    def _current_fqn(self) -> Optional[str]:
        if not self.current_func_stack:
            return None
        parts = [self.module] + self.current_class_stack + self.current_func_stack
        return ".".join(parts)

    def _resolve_in_module(self, name: str) -> Optional[str]:
        # 优先同模块同名函数
        if name in self.module_index.get(self.module, set()):
            fqn = ".".join([self.module, name])
            if fqn in self.index_all_funcs:
                return fqn
        # 也可能是外部定义的，但我们不解析 import，保守返回 None
        return None

    def _resolve_in_current_class(self, method: str) -> Optional[str]:
        if not self.current_class_stack:
            return None
        cls = self.current_class_stack[-1]
        if method in self.class_index.get((self.module, cls), set()):
            fqn = ".".join([self.module, cls, method])
            if fqn in self.index_all_funcs:
                return fqn
        return None

    def _resolve_in_named_class(self, cls_name: str, method: str) -> Optional[str]:
        if method in self.class_index.get((self.module, cls_name), set()):
            fqn = ".".join([self.module, cls_name, method])
            if fqn in self.index_all_funcs:
                return fqn
        return None

    def visit_ClassDef(self, node: ast.ClassDef):
        self.current_class_stack.append(node.name)
        self.generic_visit(node)
        self.current_class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.current_func_stack.append(node.name)
        self.generic_visit(node)
        self.current_func_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.visit_FunctionDef(node)

    def visit_Call(self, node: ast.Call):
        caller = self._current_fqn()
        if caller:
            callee_fqn = None
            # 1) foo(...)
            if isinstance(node.func, ast.Name):
                callee_fqn = self._resolve_in_module(node.func.id)
            # 2) self.foo(...) / obj.foo(...)
            elif isinstance(node.func, ast.Attribute):
                attr = node.func.attr
                # self.foo()
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                    callee_fqn = self._resolve_in_current_class(attr)
                # ClassName.foo()
                elif isinstance(node.func.value, ast.Name):
                    callee_fqn = self._resolve_in_named_class(node.func.value.id, attr)
                # 其它复杂情况忽略
            if callee_fqn:
                self.edges.append((caller, callee_fqn, getattr(node, "lineno", -1)))
        self.generic_visit(node)

def build_indexes(root: str, files: List[str]):
    all_funcs: Dict[str, FuncDef] = {}
    module_to_funcs: Dict[str, set] = {}
    class_to_methods: Dict[Tuple[str, str], set] = {}

    for fp in files:
        src = read_text(fp)
        try:
            tree = ast.parse(src, filename=fp, type_comments=True)
        except SyntaxError:
            continue
        module = rel_module_name(root, fp)
        idx = Indexer(root, fp, module, src)
        idx.visit(tree)
        all_funcs.update(idx.func_defs)
        # 合并索引
        for m, s in idx.module_index.items():
            module_to_funcs.setdefault(m, set()).update(s)
        for k, s in idx.class_index.items():
            class_to_methods.setdefault(k, set()).update(s)
    return all_funcs, module_to_funcs, class_to_methods

def collect_edges(root: str, files: List[str], all_funcs, module_index, class_index):
    edges: List[Tuple[str, str, str, int]] = []  # caller, callee, file, line
    for fp in files:
        src = read_text(fp)
        try:
            tree = ast.parse(src, filename=fp, type_comments=True)
        except SyntaxError:
            continue
        module = rel_module_name(root, fp)
        cc = CallCollector(module, fp, all_funcs, module_index, class_index)
        cc.visit(tree)
        for (caller, callee, line) in cc.edges:
            edges.append((caller, callee, os.path.relpath(fp, root), line))
    # 去重
    seen = set()
    uniq = []
    for e in edges:
        if e not in seen:
            seen.add(e)
            uniq.append(e)
    return uniq

def main():
    if len(sys.argv) < 2:
        print("Usage: python callgraph_pyrepo.py <project_dir> [out_dir]")
        sys.exit(1)
    root = os.path.abspath(sys.argv[1])
    out_dir = os.path.abspath(sys.argv[2]) if len(sys.argv) >= 3 else os.path.join(root, ".cg_out")
    os.makedirs(out_dir, exist_ok=True)

    files = find_py_files(root)
    all_funcs, module_index, class_index = build_indexes(root, files)
    edges = collect_edges(root, files, all_funcs, module_index, class_index)

    # 导出 functions.json
    funcs_json = {
        fqn: {
            "file": os.path.relpath(fd.file, root),
            "start": fd.start,
            "end": fd.end,
            "code": fd.code
        } for fqn, fd in all_funcs.items()
    }
    with open(os.path.join(out_dir, "functions.json"), "w", encoding="utf-8") as f:
        json.dump(funcs_json, f, ensure_ascii=False, indent=2)

    # 导出 edges.csv
    with open(os.path.join(out_dir, "edges.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["caller", "callee", "file", "line"])
        for caller, callee, file_rel, line in edges:
            w.writerow([caller, callee, file_rel, line])

    # 简短报告
    print(f"[done] scanned {len(files)} files")
    print(f"[done] functions: {len(all_funcs)}")
    print(f"[done] edges: {len(edges)}")
    print(f"[out] {os.path.join(out_dir, 'functions.json')}")
    print(f"[out] {os.path.join(out_dir, 'edges.csv')}")

if __name__ == "__main__":
    main()
