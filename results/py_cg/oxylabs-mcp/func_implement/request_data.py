# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.request_data
# lines: 49-50
def request_data():
    return Request("POST", "https://example.com/v1/queries")