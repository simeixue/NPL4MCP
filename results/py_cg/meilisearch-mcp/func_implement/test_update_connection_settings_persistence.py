# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue16GetDocumentsJsonSerialization.test_update_connection_settings_persistence
# lines: 385-408
    async def test_update_connection_settings_persistence(self, mcp_server):
        """Test that connection updates persist for MCP client sessions"""
        # Test URL update
        await simulate_mcp_call(
            mcp_server, "update-connection-settings", {"url": ALT_TEST_URL}
        )
        assert mcp_server.url == ALT_TEST_URL
        assert mcp_server.meili_client.client.config.url == ALT_TEST_URL

        # Test API key update
        await simulate_mcp_call(
            mcp_server, "update-connection-settings", {"api_key": TEST_API_KEY}
        )
        assert mcp_server.api_key == TEST_API_KEY
        assert mcp_server.meili_client.client.config.api_key == TEST_API_KEY

        # Test both updates together
        await simulate_mcp_call(
            mcp_server,
            "update-connection-settings",
            {"url": ALT_TEST_URL_2, "api_key": FINAL_TEST_KEY},
        )
        assert mcp_server.url == ALT_TEST_URL_2
        assert mcp_server.api_key == FINAL_TEST_KEY