# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_server_creation
# lines: 5-9
def test_server_creation():
    """Test that we can create a server instance"""
    server = create_server()
    assert server is not None
    assert server.meili_client is not None