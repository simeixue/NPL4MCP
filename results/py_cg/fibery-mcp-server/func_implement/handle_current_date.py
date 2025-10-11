# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/current_date.py
# module: src.fibery_mcp_server.tools.current_date
# qname: src.fibery_mcp_server.tools.current_date.handle_current_date
# lines: 17-19
async def handle_current_date() -> List[mcp.types.TextContent]:
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return [mcp.types.TextContent(type="text", text=date)]