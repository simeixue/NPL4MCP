#!/usr/bin/env python3
import asyncio
import inspect
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional

from fastmcp import Client
from fastmcp.tools import FunctionTool
from utils.file_util import FileUtil

REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE = Path("/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg")

# ---------------- Server config ----------------
config = {
    "mcpServers": {
        "mcp-aiven": {
            "command": "uv",
            "args": [
                "--directory",
                f"{REPO_BASE}/mcp-aiven",
                "run",
                "--with-editable",
                f"{REPO_BASE}/mcp-aiven",
                "--python",
                "3.13",
                "mcp-aiven",
            ],
            "env": {
                "AIVEN_BASE_URL": "https://api.aiven.io",
                "AIVEN_TOKEN": os.environ.get("AIVEN_TOKEN", ""),
            },
        },
        "chronulus-mcp": {
            "command": "uvx",
            "args": ["chronulus-mcp"],
            "env": {"CHRONULUS_API_KEY": os.environ.get("CHRONULUS_API_KEY", "")},
        },
        "meilisearch-mcp": {
            "command": "uvx",
            "args": ["-n", "meilisearch-mcp"]
        },
        
        # "MiniMax-MCP": {
        #     "command": "uvx",
        #     "args": ["minimax-mcp", "-y"],
        #     "env": {
        #         "MINIMAX_API_KEY": os.environ.get("MINIMAX_API_KEY", ""),
        #         "MINIMAX_MCP_BASE_PATH": os.environ.get("MINIMAX_MCP_BASE_PATH", ""),
        #         "MINIMAX_API_HOST": os.environ.get("MINIMAX_API_HOST", ""),
        #         "MINIMAX_API_RESOURCE_MODE": os.environ.get(
        #             "MINIMAX_API_RESOURCE_MODE", ""
        #         ),
        #     },
        # },
    }
}

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
    解析 code2flow 风格 JSON:
    {
      "graph": {
        "nodes": { "node_x": {"name": "pkg::func"} ... },
        "edges": [ {"source":"node_x","target":"node_y"} ... ]
      }
    }
    返回: (caller->set(callee), uid->func_name)
    """
    callers: Dict[str, Set[str]] = {}
    uid2name: Dict[str, str] = {}
    if not cg_path.exists():
        return callers, uid2name

    try:
        data = json.loads(_read_text(cg_path))
    except Exception:
        return callers, uid2name

    graph = data.get("graph") or {}
    nodes = graph.get("nodes") or {}
    edges = graph.get("edges") or []

    # node 名优先 nodes[*].name，形如 "pkg::func"
    for uid, node in nodes.items():
        name = (node or {}).get("name", "") or ""
        func = name.split("::")[-1] if "::" in name else name
        if not func:
            # 退化：尝试从 label 提取 "xxx()"
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

def serialize_tool(tool, proj_name: str, impl_map: Dict[str, str]) -> dict:
    name = getattr(tool, "name", None) or getattr(tool, "tool_name", None)
    desc = getattr(tool, "description", None)
    schema = _get_schema(tool)
    ann = _get_annotations(tool)

    impl = select_impl_for_tool(str(name), impl_map)
    if impl is None:
        impl = fallback_source(tool)

    return {
        "name": name,
        "description": desc,
        "input_schema": schema,
        "annotations": ann,
        "implementation": impl,
    }

# ---------------- Per-server run ----------------
async def handle_one_server(server_name: str, server_cfg: dict):
    client = Client({"mcpServers": {server_name: server_cfg}})
    async with client:
        print(f"[connect] {server_name}: {client.is_connected()}")
        tools = await client.list_tools()

    impl_map = build_impl_map(server_name)
    out_dir = OUT_BASE / server_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "tools_with_impl.json"

    serializable = [serialize_tool(t, server_name, impl_map) for t in tools]
    FileUtil.save_data(serializable, str(out_path), indent=2)
    print(f"[ok] {server_name} -> {out_path}")

async def main():
    for name, cfg in config["mcpServers"].items():
        await handle_one_server(name, cfg)

if __name__ == "__main__":
    asyncio.run(main())
