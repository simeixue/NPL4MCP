# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_current_time
# lines: 76-82
def test_get_current_time(test_time, timezone, expected):
    with freeze_time(test_time):
        time_server = TimeServer()
        result = time_server.get_current_time(timezone)
        assert result.timezone == expected["timezone"]
        assert result.datetime == expected["datetime"]
        assert result.is_dst == expected["is_dst"]