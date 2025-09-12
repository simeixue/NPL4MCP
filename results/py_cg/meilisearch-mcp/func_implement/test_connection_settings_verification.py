# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPClientIntegration.test_connection_settings_verification
# lines: 156-175
    async def test_connection_settings_verification(self, mcp_server):
        """Test connection settings tools to verify MCP client can connect to server"""
        # Test getting current connection settings
        result = await simulate_mcp_call(mcp_server, "get-connection-settings")
        text = assert_text_content_response(result, "Current connection settings:")
        assert "URL:" in text

        # Test updating connection settings
        update_result = await simulate_mcp_call(
            mcp_server, "update-connection-settings", {"url": ALT_TEST_URL}
        )
        update_text = assert_text_content_response(
            update_result, "Successfully updated connection settings"
        )
        assert ALT_TEST_URL in update_text

        # Verify the update took effect
        verify_result = await simulate_mcp_call(mcp_server, "get-connection-settings")
        verify_text = assert_text_content_response(verify_result)
        assert ALT_TEST_URL in verify_text