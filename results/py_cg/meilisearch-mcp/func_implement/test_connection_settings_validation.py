# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue16GetDocumentsJsonSerialization.test_connection_settings_validation
# lines: 410-423
    async def test_connection_settings_validation(self, mcp_server):
        """Test that MCP client receives validation for connection settings"""
        # Test with empty updates
        result = await simulate_mcp_call(mcp_server, "update-connection-settings", {})
        assert_text_content_response(result, "Successfully updated")

        # Test partial updates
        original_url = mcp_server.url
        await simulate_mcp_call(
            mcp_server, "update-connection-settings", {"api_key": "new_key_only"}
        )

        assert mcp_server.url == original_url  # URL unchanged
        assert mcp_server.api_key == "new_key_only"  # Key updated