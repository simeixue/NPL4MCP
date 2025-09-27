# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_local_tz_with_valid_iana_name
# lines: 479-484
def test_get_local_tz_with_valid_iana_name(mock_get_localzone):
    """Test that valid IANA timezone names from tzlocal work correctly."""
    mock_get_localzone.return_value = "Europe/London"
    result = get_local_tz()
    assert str(result) == "Europe/London"
    assert isinstance(result, ZoneInfo)