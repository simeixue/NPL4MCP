# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_current_time_with_invalid_timezone
# lines: 85-91
def test_get_current_time_with_invalid_timezone():
    time_server = TimeServer()
    with pytest.raises(
        McpError,
        match=r"Invalid timezone: 'No time zone found with key Invalid/Timezone'",
    ):
        time_server.get_current_time("Invalid/Timezone")