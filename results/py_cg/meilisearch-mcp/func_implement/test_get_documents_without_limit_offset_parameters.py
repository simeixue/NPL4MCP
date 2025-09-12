# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue17DefaultLimitOffset.test_get_documents_without_limit_offset_parameters
# lines: 429-445
    async def test_get_documents_without_limit_offset_parameters(self, mcp_server):
        """Test that get-documents works without providing limit/offset parameters (issue #17)"""
        test_index = generate_unique_index_name("test_issue17")
        test_documents = [
            {"id": 1, "title": "Test Document 1", "content": "Content 1"},
            {"id": 2, "title": "Test Document 2", "content": "Content 2"},
            {"id": 3, "title": "Test Document 3", "content": "Content 3"},
        ]

        # Create index and add test documents
        await create_test_index_with_documents(mcp_server, test_index, test_documents)

        # Test get-documents without any limit/offset parameters (should use defaults)
        result = await simulate_mcp_call(
            mcp_server, "get-documents", {"indexUid": test_index}
        )
        assert_text_content_response(result, "Documents:")