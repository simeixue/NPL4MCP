# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/test/time_server_test.py
# module: src.time.test.time_server_test
# qname: src.time.test.time_server_test.test_get_local_tz_with_invalid_override
# lines: 472-475
def test_get_local_tz_with_invalid_override():
    """Test that invalid timezone override raises an error."""
    with pytest.raises(Exception):  # ZoneInfo will raise an exception
        get_local_tz("Invalid/Timezone")