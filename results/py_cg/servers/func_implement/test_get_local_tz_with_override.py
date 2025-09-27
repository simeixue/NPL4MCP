# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_local_tz_with_override
# lines: 465-469
def test_get_local_tz_with_override():
    """Test that timezone override works correctly."""
    result = get_local_tz("America/New_York")
    assert str(result) == "America/New_York"
    assert isinstance(result, ZoneInfo)