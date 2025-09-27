# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_local_tz_when_none_returned
# lines: 488-492
def test_get_local_tz_when_none_returned(mock_get_localzone):
    """Test default to UTC when tzlocal returns None."""
    mock_get_localzone.return_value = None
    result = get_local_tz()
    assert str(result) == "UTC"