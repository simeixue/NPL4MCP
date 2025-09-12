# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/utils.py
# module: minimax_mcp.utils
# qname: minimax_mcp.utils.is_installed
# lines: 143-144
def is_installed(lib_name: str) -> bool:
    return shutil.which(lib_name) is not None