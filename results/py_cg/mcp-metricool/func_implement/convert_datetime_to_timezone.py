# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.convert_datetime_to_timezone
# lines: 823-830
def convert_datetime_to_timezone(dt_str: str, target_tz_str: str) -> str:
    try:
        dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S%z")
        target_tz = timezone(target_tz_str)
        dt_converted = dt.astimezone(target_tz)
        return dt_converted.isoformat()
    except Exception as e:
        return dt_str