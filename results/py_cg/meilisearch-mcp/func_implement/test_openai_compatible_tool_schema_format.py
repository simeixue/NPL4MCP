# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue27OpenAISchemaCompatibility.test_openai_compatible_tool_schema_format
# lines: 698-721
    async def test_openai_compatible_tool_schema_format(self, mcp_server):
        """Test that tool schemas follow OpenAI function calling format (issue #27)"""
        tools = await simulate_list_tools(mcp_server)

        for tool in tools:
            # Verify tool has required OpenAI attributes
            assert hasattr(tool, "name")
            assert hasattr(tool, "description")
            assert hasattr(tool, "inputSchema")

            # Verify schema structure matches OpenAI expectations
            schema = tool.inputSchema
            assert isinstance(schema, dict)
            assert schema.get("type") == "object"
            assert "properties" in schema
            assert isinstance(schema["properties"], dict)

            # If tool has required parameters, they should be in required array
            if "required" in schema:
                assert isinstance(schema["required"], list)

                # All required fields should exist in properties
                for required_field in schema["required"]:
                    assert required_field in schema["properties"]