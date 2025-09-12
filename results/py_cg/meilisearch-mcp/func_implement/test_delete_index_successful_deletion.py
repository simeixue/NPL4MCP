# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue23DeleteIndexTool.test_delete_index_successful_deletion
# lines: 508-534
    async def test_delete_index_successful_deletion(self, mcp_server):
        """Test successful index deletion through MCP client (issue #23)"""
        test_index = generate_unique_index_name("test_delete_success")

        # Create index first
        await simulate_mcp_call(mcp_server, "create-index", {"uid": test_index})
        await wait_for_indexing()

        # Verify index exists by listing indexes
        list_result = await simulate_mcp_call(mcp_server, "list-indexes")
        list_text = assert_text_content_response(list_result)
        assert test_index in list_text

        # Delete the index
        result = await simulate_mcp_call(
            mcp_server, "delete-index", {"uid": test_index}
        )
        response_text = assert_text_content_response(
            result, "Successfully deleted index:"
        )
        assert test_index in response_text

        # Verify index no longer exists by listing indexes
        await wait_for_indexing()
        list_result_after = await simulate_mcp_call(mcp_server, "list-indexes")
        list_text_after = assert_text_content_response(list_result_after)
        assert test_index not in list_text_after