# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/src/mcp_server_time/server.py
# module: src.time.src.mcp_server_time.server
# qname: src.time.src.mcp_server_time.server.get_zoneinfo
# lines: 53-57
def get_zoneinfo(timezone_name: str) -> ZoneInfo:
    try:
        return ZoneInfo(timezone_name)
    except Exception as e:
        raise McpError(f"Invalid timezone: {str(e)}")