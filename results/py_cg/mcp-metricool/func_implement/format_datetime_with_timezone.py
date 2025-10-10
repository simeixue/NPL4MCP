# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.format_datetime_with_timezone
# lines: 816-821
def format_datetime_with_timezone(date_str: str, hour: str, timezone_str: str) -> str:
    tz_clean = unquote(timezone_str)
    tz = timezone(tz_clean)
    dt = datetime.strptime(f"{date_str}T{hour}", "%Y-%m-%dT%H:%M:%S")
    final_dt = tz.localize(dt)
    return quote(final_dt.isoformat())