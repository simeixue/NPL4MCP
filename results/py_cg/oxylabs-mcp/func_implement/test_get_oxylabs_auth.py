# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/unit/test_utils.py
# module: tests.unit.test_utils
# qname: tests.unit.test_utils.test_get_oxylabs_auth
# lines: 30-35
def test_get_oxylabs_auth(env_vars):
    with patch("os.environ", new=env_vars):
        settings.MCP_TRANSPORT = "stdio"
        username, password = get_oxylabs_auth()
        assert username == env_vars.get("OXYLABS_USERNAME")
        assert password == env_vars.get("OXYLABS_PASSWORD")