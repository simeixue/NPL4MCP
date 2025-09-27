# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/time/src/mcp_server_time/server.py
# module: src.mcp_server_time.server
# qname: src.mcp_server_time.server.TimeServer.get_current_time
# lines: 61-71
    def get_current_time(self, timezone_name: str) -> TimeResult:
        """Get current time in specified timezone"""
        timezone = get_zoneinfo(timezone_name)
        current_time = datetime.now(timezone)

        return TimeResult(
            timezone=timezone_name,
            datetime=current_time.isoformat(timespec="seconds"),
            day_of_week=current_time.strftime("%A"),
            is_dst=bool(current_time.dst()),
        )