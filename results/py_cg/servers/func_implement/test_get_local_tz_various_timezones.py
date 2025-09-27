# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_local_tz_various_timezones
# lines: 523-528
def test_get_local_tz_various_timezones(mock_get_localzone, timezone_name):
    """Test various timezone names that tzlocal might return."""
    mock_get_localzone.return_value = timezone_name
    result = get_local_tz()
    assert str(result) == timezone_name
    assert isinstance(result, ZoneInfo)