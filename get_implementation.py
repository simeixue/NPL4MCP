from fastmcp import Client
from fastmcp.tools import FunctionTool
import inspect
import asyncio
import os, io, json, re
from pathlib import Path
from utils.file_util import FileUtil

# 根目录
REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE = "/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg"

# ----------------------
# 工具函数
# ----------------------
def load_func_slices(func_dir: Path):
    """读取func_implement目录，返回 by_qname/by_name"""
    by_qname, by_name = {}, {}
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
        body = text
        if qname:
            by_qname[qname] = body
            simple = qname.split(".")[-1]
            by_name.setdefault(simple, []).append(body)
        else:
            simple = f.stem
            by_name.setdefault(simple, []).append(body)
    return by_qname, by_name

def load_cg_edges(cg_path: Path):
    """读取调用关系json，返回edges列表"""
    if not cg_path.exists():
        return []
    try:
        data = json.loads(cg_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    edges = []
    if "edges" in data:
        for e in data["edges"]:
            if isinstance(e, dict):
                edges.append((e["caller"], e["callee"]))
            elif isinstance(e, list) and len(e) == 2:
                edges.append((e[0], e[1]))
    return edges

def build_callee_index(edges):
    idx = {}
    for a,b in edges:
        idx.setdefault(a,set()).add(b)
    return idx

def pick_impl(tool, by_qname, by_name):
    """根据 tool.name 匹配函数实现"""
    n = tool.name
    if n in by_name:
        return n, by_name[n][0]
    simple = n.replace("-", "_")
    if simple in by_name:
        return simple, by_name[simple][0]
    return None, None

def make_implementation(main_body, callees, by_qname, by_name):
    impl = [main_body.rstrip()]
    for c in callees:
        body = by_qname.get(c)
        if not body:
            last = c.split(".")[-1]
            lst = by_name.get(last)
            if lst:
                body = lst[0]
        if body:
            impl.append("\n#callee:\n" + body.rstrip())
    return "\n\n".join(impl) + "\n"

# ----------------------
# 工具对象序列化
# ----------------------
def serialize_tool(tool, proj_name):
    # tool 的函数体
    source = None
    if isinstance(tool, FunctionTool):
        f = getattr(tool, "function", None) or getattr(tool, "fn", None)
        if f:
            try:
                source = inspect.getsource(f)
            except Exception:
                pass

    # 尝试拼接调用关系
    func_dir = Path(OUT_BASE)/proj_name/"func_implement"
    cg_path = Path(OUT_BASE)/proj_name/"cg_py.json"
    by_qname, by_name = load_func_slices(func_dir)
    edges = load_cg_edges(cg_path)
    callee_idx = build_callee_index(edges)

    fq, body = pick_impl(tool, by_qname, by_name)
    if body:
        callees = []
        if fq:
            callees.extend(list(callee_idx.get(fq, [])))
            if "." in fq:
                callees.extend(list(callee_idx.get(fq.split(".")[-1], [])))
        implementation = make_implementation(body, callees, by_qname, by_name)
    else:
        implementation = source  # 退化：只用 inspect 的结果

    return {
        "name": tool.name,
        "description": tool.description,
        "implementation": implementation,
        "input_schema": tool.inputSchema,
        "annotations": tool.annotations,
    }

# ----------------------
# 配置和主流程
# ----------------------
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
                "mcp-aiven"
            ],
            "env": {
                "AIVEN_BASE_URL": "https://api.aiven.io",
                "AIVEN_TOKEN": "$AIVEN_TOKEN"
            }
        },
        "chronulus-mcp": {
            "command": "uvx",
            "args": ["chronulus-mcp"],
            "env": {
                "CHRONULUS_API_KEY": "<YOUR_CHRONULUS_API_KEY>"
            }
        },
        "MiniMax-MCP": {
            "command": "uvx",
            "args": [
                "minimax-mcp",
                "-y"
            ],
            "env": {
                "MINIMAX_API_KEY": "insert-your-api-key-here",
                "MINIMAX_MCP_BASE_PATH": "local-output-dir-path, such as /User/xxx/Desktop",
                "MINIMAX_API_HOST": "api host, https://api.minimax.io | https://api.minimaxi.com",
                "MINIMAX_API_RESOURCE_MODE": "optional, [url|local], url is default, audio/image/video are downloaded locally or provided in URL format"
            }
        }
    }
}

client = Client(config)

async def main():
    async with client:
        print(f"Client connected: {client.is_connected()}")
        all_tools = await client.list_tools()

    # 遍历每个 server
    for proj_name in config["mcpServers"].keys():
        # 注意：all_tools 可能包含多个 server 的工具，
        # 如果 fastmcp 没分隔，就需要你按 server 来调用 client.list_tools(server_id=proj_name)
        tools = all_tools  

        serializable_tools = [serialize_tool(t, proj_name) for t in tools]

        out_dir = Path(OUT_BASE) / proj_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "tools_with_impl.json"
        FileUtil.save_data(serializable_tools, str(out_path), indent=2)
        print(f"[ok] {proj_name} -> {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
