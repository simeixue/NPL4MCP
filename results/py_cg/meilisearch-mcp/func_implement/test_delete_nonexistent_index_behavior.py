# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue23DeleteIndexTool.test_delete_nonexistent_index_behavior
# lines: 569-581
    async def test_delete_nonexistent_index_behavior(self, mcp_server):
        """Test behavior when deleting non-existent index (issue #23)"""
        nonexistent_index = generate_unique_index_name("nonexistent")

        # Try to delete non-existent index
        # Note: Meilisearch allows deleting non-existent indexes without error
        result = await simulate_mcp_call(
            mcp_server, "delete-index", {"uid": nonexistent_index}
        )
        response_text = assert_text_content_response(
            result, "Successfully deleted index:"
        )
        assert nonexistent_index in response_text