#!/usr/bin/env python3
import os, json, re, io, sys, subprocess, time, signal
from pathlib import Path

BASE = Path("/Users/xue/workspace/mcp_project/NPL4MCP")
REPOS_DIR = Path("/Users/xue/workspace/mcp_project/mcp_server_pyrepos")
OUT_BASE = BASE / "results" / "py_cg"

# ---------- fastmcp stdio client ----------
# 需要: pip install fastmcp
try:
    from fastmcp import Client  # type: ignore
except Exception as e:
    print("缺少 fastmcp: pip install fastmcp", file=sys.stderr); sys.exit(1)

def guess_server_cmd(proj_dir: Path) -> list[str] | None:
    """
    尽量通用地猜测 server 启动命令：
    1) 优先找 src/<pkg>/server.py -> python -m <pkg>.server
    2) 其次直接找任意 server.py -> python <path/to/server.py>
    3) 若是 Node server，可自行补充
    """
    # 优先 pattern: src/<pkg>/**/server.py
    for p in proj_dir.rglob("server.py"):
        try:
            # 只选在 src/ 下的
            if "src" in p.parts:
                idx = p.parts.index("src")
                module = ".".join(p.parts[idx+1:]).removesuffix(".py")
                return ["python", "-m", module]
        except ValueError:
            pass
    # 兜底：任意 server.py
    for p in proj_dir.rglob("server.py"):
        return ["python", str(p)]
    return None

def list_tools_via_fastmcp(proj_dir: Path, timeout=20) -> list[dict]:
    cmd = guess_server_cmd(proj_dir)
    if not cmd:
        return []
    # 以子进程方式启动，走 stdio
    client = Client()
    proc = client.connect_stdio(cmd=cmd)
    try:
        deadline = time.time() + timeout
        # 等待 server ready（简单轮询）
        while time.time() < deadline and not client.is_connected():
            time.sleep(0.2)
        if not client.is_connected():
            return []
        tools = client.list_tools()  # 返回 list[Tool]; 兼容成 dict
        out = []
        for t in tools:
            # 兼容 fastmcp 不同版本属性名
            name = getattr(t, "name", None) or t.get("name")
            desc = getattr(t, "description", None) or t.get("description")
            schema = getattr(t, "input_schema", None) or getattr(t, "inputSchema", None) or t.get("input_schema") or t.get("inputSchema")
            ann = getattr(t, "annotations", None) or t.get("annotations") or {}
            out.append({
                "name": name, "description": desc,
                "input_schema": schema, "annotations": ann
            })
        return out
    except Exception:
        return []
    finally:
        try:
            client.close()
        except Exception:
            pass
        # 确保子进程退出
        try:
            if proc and proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    proc.kill()
        except Exception:
            pass

# ---------- 读取函数体切片 ----------
def load_func_slices(func_dir: Path):
    """
    返回两个索引：
      by_qname: qname -> body
      by_name:  basename(最后一段) -> [bodies]
    切片文件头部形如：
      # qname: pkg.mod.Class.func
    """
    by_qname: dict[str, str] = {}
    by_name: dict[str, list[str]] = {}
    if not func_dir.exists():
        return by_qname, by_name

    for f in func_dir.glob("*.py"):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        qname = None
        for line in text.splitlines():
            if line.startswith("# qname:"):
                qname = line.split(":", 1)[1].strip()
                break
        body = text  # 含头部元信息，一并保留
        if qname:
            by_qname[qname] = body
            simple = qname.split(".")[-1]
            by_name.setdefault(simple, []).append(body)
        else:
            # 没有头就用文件名推断
            simple = f.stem
            by_name.setdefault(simple, []).append(body)
    return by_qname, by_name

# ---------- 读取调用图 ----------
def load_cg_edges(cg_path: Path) -> list[tuple[str, str]]:
    """
    尽量兼容多种 JSON 结构：
      {"edges":[{"caller":"a","callee":"b"}, ...]}
      或 code2flow 风格 {"links":[{"source": "...","target":"..."}], ...}
      或 {"edges":[["a","b"], ...]}
    """
    if not cg_path.exists():
        return []
    try:
        data = json.loads(cg_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    edges: list[tuple[str, str]] = []
    if "edges" in data:
        for e in data["edges"]:
            if isinstance(e, dict) and "caller" in e and "callee" in e:
                edges.append((e["caller"], e["callee"]))
            elif isinstance(e, list) and len(e) == 2:
                edges.append((e[0], e[1]))
    if not edges and "links" in data:
        for e in data["links"]:
            s = e.get("source"); t = e.get("target")
            if s and t:
                edges.append((s, t))
    return edges

def build_callee_index(edges: list[tuple[str, str]]):
    idx: dict[str, set[str]] = {}
    for a, b in edges:
        idx.setdefault(a, set()).add(b)
    return idx

# ---------- 将 tool 绑定到实现函数 ----------
def normalize_name(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', s.lower()) if s else ""

def pick_impl_for_tool(tool: dict, by_qname: dict[str, str], by_name: dict[str, list[str]]):
    """
    绑定顺序：
      1) annotations 里若有 qname/impl/handler 明确指向（完整限定名），直接用
      2) 用 tool.name 的简化形式在 by_name 里匹配
      3) 失败则返回 None
    """
    ann = tool.get("annotations") or {}
    for key in ("qname", "impl", "implementation", "handler", "function"):
        val = ann.get(key)
        if isinstance(val, str):
            if val in by_qname:
                return val, by_qname[val]
            # 兼容 module.fn 指向：尝试末段匹配
            last = val.split(".")[-1]
            lst = by_name.get(last)
            if lst:
                return val, lst[0]

    # 用 name 猜
    n = tool.get("name") or ""
    cand = by_name.get(n) or by_name.get(n.replace("-", "_")) or None
    if cand:
        return n, cand[0]

    # 用归一化比较
    target = normalize_name(n)
    for k, lst in by_name.items():
        if normalize_name(k) == target and lst:
            return k, lst[0]

    return None, None

# ---------- 组装 implementation ----------
def make_implementation(main_body: str, callees: list[str], by_qname: dict[str, str], by_name: dict[str, list[str]]) -> str:
    impl = [main_body.rstrip()]
    for c in callees:
        # 先按 qname，再按末段名
        body = by_qname.get(c)
        if not body:
            last = c.split(".")[-1]
            lst = by_name.get(last)
            if lst:
                body = lst[0]
        if body:
            impl.append("\n#callee:\n" + body.rstrip())
    return "\n\n".join(impl) + "\n"

# ---------- 主流程 ----------
def process_project(proj_dir: Path):
    proj_name = proj_dir.name
    out_dir = OUT_BASE / proj_name
    func_dir = out_dir / "func_implement"
    cg_path = out_dir / "cg_py.json"
    tools_out = out_dir / "tools_with_impl.json"

    by_qname, by_name = load_func_slices(func_dir)
    edges = load_cg_edges(cg_path)
    callee_idx = build_callee_index(edges)

    tools = list_tools_via_fastmcp(proj_dir)
    enriched = []
    for t in tools:
        fq, body = pick_impl_for_tool(t, by_qname, by_name)
        if not body:
            t["implementation"] = None
            enriched.append(t); continue

        # 找直接被调用的函数名列表（尽力匹配：用 fq 或其末段）
        callees = []
        keys = []
        if fq: keys.append(fq)
        # 末段名也尝试
        if fq and "." in fq: keys.append(fq.split(".")[-1])

        seen = set()
        for k in keys:
            for c in callee_idx.get(k, []):
                if c not in seen:
                    seen.add(c)
                    callees.append(c)

        t["implementation"] = make_implementation(body, callees, by_qname, by_name)
        enriched.append(t)

    tools_out.parent.mkdir(parents=True, exist_ok=True)
    tools_out.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] {proj_name} -> {tools_out}")

def main():
    for proj in REPOS_DIR.iterdir():
        if proj.is_dir():
            process_project(proj)

if __name__ == "__main__":
    main()
