# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPClientIntegration.test_tool_error_handling
# lines: 189-193
    async def test_tool_error_handling(self, mcp_server):
        """Test that MCP client receives proper error responses from server"""
        result = await simulate_mcp_call(mcp_server, "non-existent-tool")
        text = assert_text_content_response(result, "Error:")
        assert "Unknown tool" in text