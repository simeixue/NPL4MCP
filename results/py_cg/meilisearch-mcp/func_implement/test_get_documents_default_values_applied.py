# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue17DefaultLimitOffset.test_get_documents_default_values_applied
# lines: 467-487
    async def test_get_documents_default_values_applied(self, mcp_server):
        """Test that default values (offset=0, limit=20) are properly applied"""
        test_index = generate_unique_index_name("test_issue17_defaults")
        test_documents = [{"id": i, "title": f"Document {i}"} for i in range(1, 6)]

        # Create index and add test documents
        await create_test_index_with_documents(mcp_server, test_index, test_documents)

        # Test that both calls with and without parameters work
        result_no_params = await simulate_mcp_call(
            mcp_server, "get-documents", {"indexUid": test_index}
        )
        result_with_defaults = await simulate_mcp_call(
            mcp_server,
            "get-documents",
            {"indexUid": test_index, "offset": 0, "limit": 20},
        )

        # Both should work and return similar results
        assert_text_content_response(result_no_params)
        assert_text_content_response(result_with_defaults)