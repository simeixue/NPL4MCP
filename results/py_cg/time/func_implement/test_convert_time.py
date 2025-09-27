# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/time/test/time_server_test.py
# module: test.time_server_test
# qname: test.time_server_test.test_convert_time
# lines: 451-462
def test_convert_time(test_time, source_tz, time_str, target_tz, expected):
    with freeze_time(test_time):
        time_server = TimeServer()
        result = time_server.convert_time(source_tz, time_str, target_tz)

        assert result.source.timezone == expected["source"]["timezone"]
        assert result.target.timezone == expected["target"]["timezone"]
        assert result.source.datetime == expected["source"]["datetime"]
        assert result.target.datetime == expected["target"]["datetime"]
        assert result.source.is_dst == expected["source"]["is_dst"]
        assert result.target.is_dst == expected["target"]["is_dst"]
        assert result.time_difference == expected["time_difference"]