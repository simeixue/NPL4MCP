# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.mcp_server
# lines: 97-104
async def mcp_server():
    """Shared fixture for creating MCP server instances"""
    url = os.getenv("MEILI_HTTP_ADDR", TEST_URL)
    api_key = os.getenv("MEILI_MASTER_KEY")

    server = create_server(url, api_key)
    yield server
    server.cleanup()