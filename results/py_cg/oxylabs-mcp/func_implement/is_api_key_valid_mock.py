# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.is_api_key_valid_mock
# lines: 78-80
def is_api_key_valid_mock():
    with patch("oxylabs_mcp.utils.is_api_key_valid", return_value=True):
        yield