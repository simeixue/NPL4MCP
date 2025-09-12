# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue16GetDocumentsJsonSerialization.test_get_documents_returns_json_not_python_object
# lines: 347-383
    async def test_get_documents_returns_json_not_python_object(self, mcp_server):
        """Test that get-documents returns JSON-formatted text, not Python object string representation (issue #16)"""
        test_index = generate_unique_index_name("test_issue16")
        test_document = {"id": 1, "title": "Test Document", "content": "Test content"}

        # Create index and add test document
        await create_test_index_with_documents(mcp_server, test_index, [test_document])

        # Get documents with explicit parameters
        result = await simulate_mcp_call(
            mcp_server,
            "get-documents",
            {"indexUid": test_index, "offset": 0, "limit": 10},
        )

        response_text = assert_text_content_response(result, "Documents:")

        # Issue #16 assertion: Should NOT contain Python object representation
        assert (
            "<meilisearch.models.document.DocumentsResults object at"
            not in response_text
        )
        assert "DocumentsResults" not in response_text

        # Should contain actual document content
        assert "Test Document" in response_text
        assert "Test content" in response_text

        # Should be valid JSON after the "Documents:" prefix
        json_part = response_text.replace("Documents:", "").strip()
        try:
            parsed_data = json.loads(json_part)
            assert isinstance(parsed_data, dict)
            assert "results" in parsed_data
            assert len(parsed_data["results"]) > 0
        except json.JSONDecodeError:
            pytest.fail(f"get-documents returned non-JSON data: {response_text}")