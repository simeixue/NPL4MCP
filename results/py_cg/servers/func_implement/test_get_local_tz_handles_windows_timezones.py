# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_local_tz_handles_windows_timezones
# lines: 496-506
def test_get_local_tz_handles_windows_timezones(mock_get_localzone):
    """Test that tzlocal properly handles Windows timezone names.
    
    Note: tzlocal should convert Windows names like 'Pacific Standard Time'
    to proper IANA names like 'America/Los_Angeles'.
    """
    # tzlocal should return IANA names even on Windows
    mock_get_localzone.return_value = "America/Los_Angeles"
    result = get_local_tz()
    assert str(result) == "America/Los_Angeles"
    assert isinstance(result, ZoneInfo)