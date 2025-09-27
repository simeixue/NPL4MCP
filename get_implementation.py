#!/usr/bin/env python3
import asyncio
import inspect
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
import subprocess
import sys
from fastmcp import Client
from fastmcp.tools import FunctionTool
from utils.file_util import FileUtil
from utils.server_config import config

REPO_BASE = Path("/Users/xue/workspace/mcp_project/mcp_server_pyrepos")
OUT_BASE = Path("/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg")



# ---------------- Helpers: func slices + call graph ----------------
def _read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return p.read_text(encoding="utf-8", errors="ignore")

def load_func_bodies(func_dir: Path) -> Dict[str, str]:
    """func_implement 下文件名=函数名"""
    out: Dict[str, str] = {}
    if not func_dir.exists():
        return out
    for f in sorted(func_dir.glob("*.py")):
        out[f.stem] = _read_text(f)
    return out

def parse_cg_edges(cg_path: Path) -> Tuple[Dict[str, Set[str]], Dict[str, str]]:
    """
    返回:
      callers: {caller_func_name -> set(callee_func_name)}
      uid2name: {uid -> func_name}
    func_name 取 nodes[*].name 的 '::' 最后一段；若无，则从 label 的 'xxx()' 提取。
    """
    callers: Dict[str, Set[str]] = {}
    uid2name: Dict[str, str] = {}
    if not cg_path.exists():
        return callers, uid2name

    try:
        data = json.loads(_read_text(cg_path))
    except Exception:
        return callers, uid2name

    graph = (data.get("graph") or {})
    nodes = graph.get("nodes") or {}
    edges = graph.get("edges") or []

    for uid, node in nodes.items():
        name = (node or {}).get("name", "") or ""
        func = name.split("::")[-1] if "::" in name else name
        if not func:
            label = (node or {}).get("label", "")
            m = re.search(r"([A-Za-z_]\w*)\s*\(\)\s*$", str(label))
            if m:
                func = m.group(1)
        if func:
            uid2name[uid] = func

    for e in edges:
        src, tgt = e.get("source"), e.get("target")
        if not src or not tgt:
            continue
        sname, tname = uid2name.get(src), uid2name.get(tgt)
        if not sname or not tname:
            continue
        callers.setdefault(sname, set()).add(tname)

    return callers, uid2name


def load_project_indexes(proj_name: str) -> Tuple[Dict[str, str], Dict[str, Set[str]]]:
    """
    返回:
      bodies: {func_name -> 源码文本}  来自 func_implement/*.py
      callers: {caller -> set(callee)} 来自 cg_py.json
    """
    proj_dir = OUT_BASE / proj_name
    func_dir = proj_dir / "func_implement"
    cg_path = proj_dir / "cg_py.json"
    bodies = load_func_bodies(func_dir)
    callers, _ = parse_cg_edges(cg_path)
    return bodies, callers

def build_impl_map(proj_name: str) -> Dict[str, str]:
    """为项目生成 {函数名: 实现文本(含 #callee：...)}"""
    proj_dir = OUT_BASE / proj_name
    func_dir = proj_dir / "func_implement"
    cg_path = proj_dir / "cg_py.json"

    bodies = load_func_bodies(func_dir)
    callers, _ = parse_cg_edges(cg_path)

    impl_map: Dict[str, str] = {}
    for func, body in bodies.items():
        parts = [body.strip()]
        for cal in sorted(callers.get(func, [])):
            cb = bodies.get(cal)
            if cb:
                parts.append("#callee：\n" + cb.strip())
        impl_map[func] = "\n\n".join(parts) + "\n"
    return impl_map

# ---------------- Tool serialization ----------------
def _get_schema(tool) -> Optional[dict]:
    return getattr(tool, "inputSchema", None) or getattr(tool, "input_schema", None)

def _get_annotations(tool) -> dict:
    return getattr(tool, "annotations", None) or {}

def select_impl_for_tool(tool_name: str, impl_map: Dict[str, str]) -> Optional[str]:
    if tool_name in impl_map:
        return impl_map[tool_name]
    alt = tool_name.replace("-", "_")
    if alt in impl_map:
        return impl_map[alt]
    return None

def fallback_source(tool) -> Optional[str]:
    if isinstance(tool, FunctionTool):
        f = getattr(tool, "function", None) or getattr(tool, "fn", None)
        if f:
            try:
                return inspect.getsource(f)
            except Exception:
                return None
    return None

# ============ 按深度收集实现 ============
def _normalize_name(name: str) -> str:
    return (name or "").strip()

def _alt_names(name: str) -> List[str]:
    # 工具名可能含 '-'，实现文件用 '_'；做备用映射
    n = _normalize_name(name)
    alts = {n}
    if "-" in n:
        alts.add(n.replace("-", "_"))
    return list(alts)

# --- build_impl_layers ---
def build_impl_layers(start_func: str,
                      bodies: Dict[str, str],
                      callers: Dict[str, Set[str]],
                      max_depth: Optional[int] = None) -> Optional[Dict[str, object]]:
    """
    返回:
      {
        "depth_max": n,           # 收集到的最深层（仅统计实际有实现的层）
        "depth_0": str | None,    # 起点函数源码
        "depth_1": [str, ...],
        "depth_2": [str, ...],
        ...
      }
    """
    hit_name = None
    for nm in _alt_names(start_func):
        if nm in bodies:
            hit_name = nm
            break

    depth_map: Dict[str, object] = {}
    deepest = -1

    if hit_name and bodies.get(hit_name):
        depth_map["depth_0"] = bodies[hit_name]
        deepest = 0
    else:
        depth_map["depth_0"] = None

    seen: Set[str] = set()
    # 起点的第一层邻居
    start_keys = [hit_name] if hit_name else _alt_names(start_func)
    frontier: Set[str] = set()
    for sk in start_keys:
        frontier |= callers.get(sk, set())

    depth = 1
    while frontier:
        if max_depth is not None and depth > max_depth:
            break
        layer_funcs = sorted(frontier)
        layer_impls: List[str] = []
        next_frontier: Set[str] = set()

        for fn in layer_funcs:
            if fn in seen:
                continue
            seen.add(fn)
            impl = bodies.get(fn)
            if impl:
                layer_impls.append(impl)
            next_frontier |= callers.get(fn, set())

        if layer_impls:
            depth_map[f"depth_{depth}"] = layer_impls
            deepest = max(deepest, depth)

        frontier = next_frontier
        depth += 1

    # 完全没有任何实现
    has_any = (depth_map.get("depth_0") is not None) or any(k.startswith("depth_") and k != "depth_0" for k in depth_map)
    if not has_any:
        return None

    depth_map["depth_max"] = max(deepest, 0) if depth_map.get("depth_0") is not None else max(deepest, -1)
    # 若只有深层实现而 depth_0 为空，且没有任何层命中，前面已返回 None；
    # 若有深层实现但无 depth_0，则 deepest>=1，depth_max=deepest。
    return depth_map


# --- serialize_tool ---
def serialize_tool(tool, proj_name: str, bodies: Dict[str, str], callers: Dict[str, Set[str]]) -> dict:
    name = getattr(tool, "name", None) or getattr(tool, "tool_name", None)
    desc = getattr(tool, "description", None)
    schema = _get_schema(tool)
    ann = _get_annotations(tool)

    impl_layers = build_impl_layers(str(name), bodies, callers, max_depth=None)

    # depth_0 为空时，用 inspect 回填，并修正 depth_max
    if (not impl_layers) or (impl_layers.get("depth_0") is None):
        fb = fallback_source(tool)
        if fb:
            if not impl_layers:
                impl_layers = {"depth_0": fb, "depth_max": 0}
            else:
                impl_layers["depth_0"] = fb
                impl_layers["depth_max"] = max(impl_layers.get("depth_max", -1), 0)

    return {
        "name": name,
        "description": desc,
        "input_schema": schema,
        "annotations": ann,
        "implementation": impl_layers,
    }



def install_requirements(server_name: str) -> bool:
    req = REPO_BASE / server_name / "requirements.txt"
    if not req.exists():
        print(f"[deps] {server_name}: 无 requirements.txt，跳过安装")
        return False
    print(f"[deps] {server_name}: 安装依赖 -> {req}")
    rc = subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(req)]).returncode
    if rc != 0:
        print(f"[deps] {server_name}: 依赖安装失败，退出码 {rc}")
        return False
    print(f"[deps] {server_name}: 依赖安装完成")
    return True

async def try_connect_and_list(server_name: str, server_cfg: dict):
        client = Client({"mcpServers": {server_name: server_cfg}})
        async with client:
            if not client.is_connected():
                raise RuntimeError("client.is_connected() == False")
            print(f"[connect] {server_name}: {client.is_connected()}")
            tools = await client.list_tools()
            return tools

# ---------------- Per-server run ----------------
async def handle_one_server(server_name: str, server_cfg: dict):
    tools = None
    try:
        tools = await try_connect_and_list(server_name, server_cfg)
    except Exception as e:
        print(f"[connect] {server_name}: 首次连接失败: {e}")

    if not tools:
        installed = install_requirements(server_name)
        if not installed:
            print(f"[connect] {server_name}: 无法建立连接且无依赖可装")
            return
        try:
            tools = await try_connect_and_list(server_name, server_cfg)
        except Exception as e:
            print(f"[connect] {server_name}: 二次连接失败: {e}")
            return

    print(f"[tools] {server_name}: 获取到 {len(tools)} 个工具")

    # 一次性加载 bodies 与 callers
    bodies, callers = load_project_indexes(server_name)

    out_dir = OUT_BASE / server_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "tools_with_impl.json"

    serializable = [serialize_tool(t, server_name, bodies, callers) for t in tools]

    # 所有 implementation 为 None 的提示（现在 implementation 是 dict 或 None）
    if all(item.get("implementation") in (None, {}) for item in serializable):
        print(f"\033[33m{server_name}的所有 implementation 都是 None\033[0m")

    FileUtil.save_data(serializable, str(out_path), indent=2)
    print(f"[ok] {server_name} -> {out_path}")

async def main():
    for name, cfg in config["mcpServers"].items():
        await handle_one_server(name, cfg)

if __name__ == "__main__":
    asyncio.run(main())
