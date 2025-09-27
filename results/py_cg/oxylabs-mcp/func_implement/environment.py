# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.environment
# lines: 33-40
def environment():
    env = {
        "OXYLABS_USERNAME": "oxylabs_username",
        "OXYLABS_PASSWORD": "oxylabs_password",
        "OXYLABS_AI_STUDIO_API_KEY": "oxylabs_ai_studio_api_key",
    }
    with patch("os.environ", new=env):
        yield