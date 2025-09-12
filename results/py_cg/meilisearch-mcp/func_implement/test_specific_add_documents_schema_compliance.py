# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue27OpenAISchemaCompatibility.test_specific_add_documents_schema_compliance
# lines: 672-696
    async def test_specific_add_documents_schema_compliance(self, mcp_server):
        """Test add-documents schema specifically mentioned in issue #27"""
        tools = await simulate_list_tools(mcp_server)
        add_docs_tool = next(tool for tool in tools if tool.name == "add-documents")

        schema = add_docs_tool.inputSchema

        # Verify overall structure
        assert schema["type"] == "object"
        assert schema["additionalProperties"] is False
        assert "properties" in schema
        assert "required" in schema

        # Verify documents array property
        documents_prop = schema["properties"]["documents"]
        assert documents_prop["type"] == "array"
        assert (
            "items" in documents_prop
        ), "add-documents documents array missing items property"
        assert documents_prop["items"]["type"] == "object"

        # Verify required fields
        assert "indexUid" in schema["required"]
        assert "documents" in schema["required"]
        assert "primaryKey" not in schema["required"]  # Should be optional