# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/time/test/time_server_test.py
# module: test.time_server_test
# qname: test.time_server_test.test_convert_time_errors
# lines: 117-120
def test_convert_time_errors(source_tz, time_str, target_tz, expected_error):
    time_server = TimeServer()
    with pytest.raises((McpError, ValueError), match=expected_error):
        time_server.convert_time(source_tz, time_str, target_tz)