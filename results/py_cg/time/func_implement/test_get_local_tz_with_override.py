# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/time/test/time_server_test.py
# module: test.time_server_test
# qname: test.time_server_test.test_get_local_tz_with_override
# lines: 465-469
def test_get_local_tz_with_override():
    """Test that timezone override works correctly."""
    result = get_local_tz("America/New_York")
    assert str(result) == "America/New_York"
    assert isinstance(result, ZoneInfo)