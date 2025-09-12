# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue17DefaultLimitOffset.test_get_documents_with_explicit_parameters
# lines: 448-465
    async def test_get_documents_with_explicit_parameters(self, mcp_server):
        """Test that get-documents still works with explicit limit/offset parameters"""
        test_index = generate_unique_index_name("test_issue17_explicit")
        test_documents = [
            {"id": 1, "title": "Test Document 1", "content": "Content 1"},
            {"id": 2, "title": "Test Document 2", "content": "Content 2"},
        ]

        # Create index and add test documents
        await create_test_index_with_documents(mcp_server, test_index, test_documents)

        # Test get-documents with explicit parameters
        result = await simulate_mcp_call(
            mcp_server,
            "get-documents",
            {"indexUid": test_index, "offset": 0, "limit": 1},
        )
        assert_text_content_response(result, "Documents:")