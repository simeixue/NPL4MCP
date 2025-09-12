# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPConnectionSettings.test_get_connection_settings_format
# lines: 326-341
    async def test_get_connection_settings_format(self, mcp_server):
        """Test connection settings response format for MCP clients"""
        result = await simulate_mcp_call(mcp_server, "get-connection-settings")
        text = assert_text_content_response(result, "Current connection settings:")

        # Verify required fields are present
        required_fields = ["URL:", "API Key:"]
        for field in required_fields:
            assert field in text

        # Check URL is properly displayed
        assert mcp_server.url in text

        # Check API key is masked for security
        expected_key_display = "********" if mcp_server.api_key else "Not set"
        assert expected_key_display in text or "Not set" in text