# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/src/mcp_server_time/server.py
# module: src.time.src.mcp_server_time.server
# qname: src.time.src.mcp_server_time.server.get_local_tz
# lines: 41-50
def get_local_tz(local_tz_override: str | None = None) -> ZoneInfo:
    if local_tz_override:
        return ZoneInfo(local_tz_override)

    # Get local timezone from datetime.now()
    local_tzname = get_localzone_name()
    if local_tzname is not None:
        return ZoneInfo(local_tzname)
    # Default to UTC if local timezone cannot be determined
    return ZoneInfo("UTC")