# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPClientIntegration.test_health_check_tool
# lines: 177-187
    async def test_health_check_tool(self, mcp_server):
        """Test health check tool through MCP client interface"""
        # Mock the health check to avoid requiring actual Meilisearch
        with patch.object(
            mcp_server.meili_client, "health_check", new_callable=AsyncMock
        ) as mock_health:
            mock_health.return_value = True
            result = await simulate_mcp_call(mcp_server, "health-check")

            assert_text_content_response(result, "available")
            mock_health.assert_called_once()