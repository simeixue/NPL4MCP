# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue23DeleteIndexTool.test_delete_index_with_documents
# lines: 536-567
    async def test_delete_index_with_documents(self, mcp_server):
        """Test deleting index that contains documents (issue #23)"""
        test_index = generate_unique_index_name("test_delete_with_docs")
        test_documents = [
            {"id": 1, "title": "Test Document 1", "content": "Content 1"},
            {"id": 2, "title": "Test Document 2", "content": "Content 2"},
        ]

        # Create index and add documents
        await create_test_index_with_documents(mcp_server, test_index, test_documents)

        # Verify documents exist
        docs_result = await simulate_mcp_call(
            mcp_server, "get-documents", {"indexUid": test_index}
        )
        docs_text = assert_text_content_response(docs_result, "Documents:")
        assert "Test Document 1" in docs_text

        # Delete the index (should also delete all documents)
        result = await simulate_mcp_call(
            mcp_server, "delete-index", {"uid": test_index}
        )
        response_text = assert_text_content_response(
            result, "Successfully deleted index:"
        )
        assert test_index in response_text

        # Verify index and documents are gone
        await wait_for_indexing()
        list_result = await simulate_mcp_call(mcp_server, "list-indexes")
        list_text = assert_text_content_response(list_result)
        assert test_index not in list_text