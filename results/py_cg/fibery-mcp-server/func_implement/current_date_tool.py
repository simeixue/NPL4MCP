# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/current_date.py
# module: src.fibery_mcp_server.tools.current_date
# qname: src.fibery_mcp_server.tools.current_date.current_date_tool
# lines: 9-14
def current_date_tool() -> mcp.types.Tool:
    return mcp.types.Tool(
        name=current_date_tool_name,
        description="Get today's date in ISO 8601 format (YYYY-mm-dd.HH:MM:SS.000Z)",
        inputSchema={"type": "object"},
    )