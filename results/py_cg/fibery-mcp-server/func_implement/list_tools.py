# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/server.py
# module: src.fibery_mcp_server.server
# qname: src.fibery_mcp_server.server.serve.list_tools
# lines: 23-24
    async def list_tools() -> List[mcp.types.Tool]:
        return handle_list_tools()