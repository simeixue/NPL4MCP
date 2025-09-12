# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPClientIntegration.test_mcp_server_initialization
# lines: 212-224
    async def test_mcp_server_initialization(self, mcp_server):
        """Test that MCP server initializes correctly for client connections"""
        # Verify server has required attributes
        assert hasattr(mcp_server, "server")
        assert hasattr(mcp_server, "meili_client")
        assert hasattr(mcp_server, "url")
        assert hasattr(mcp_server, "api_key")
        assert hasattr(mcp_server, "logger")

        # Verify server name and basic configuration
        assert mcp_server.server.name == "meilisearch"
        assert mcp_server.url is not None
        assert mcp_server.meili_client is not None