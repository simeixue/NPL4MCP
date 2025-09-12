# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue23DeleteIndexTool.test_delete_index_input_validation
# lines: 583-588
    async def test_delete_index_input_validation(self, mcp_server):
        """Test input validation for delete-index tool (issue #23)"""
        # Test missing uid parameter
        result = await simulate_mcp_call(mcp_server, "delete-index", {})
        response_text = assert_text_content_response(result, "error:")
        assert "error:" in response_text