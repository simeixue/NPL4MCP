# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue27OpenAISchemaCompatibility.test_array_schemas_have_items_property
# lines: 639-657
    async def test_array_schemas_have_items_property(self, mcp_server):
        """Test that all array schemas include items property for OpenAI compatibility (issue #27)"""
        tools = await simulate_list_tools(mcp_server)

        tools_with_arrays = ["add-documents", "search", "get-tasks", "create-key"]

        for tool in tools:
            if tool.name in tools_with_arrays:
                schema = tool.inputSchema
                properties = schema.get("properties", {})

                for prop_name, prop_schema in properties.items():
                    if prop_schema.get("type") == "array":
                        assert (
                            "items" in prop_schema
                        ), f"Tool '{tool.name}' property '{prop_name}' missing items"
                        assert isinstance(
                            prop_schema["items"], dict
                        ), f"Tool '{tool.name}' property '{prop_name}' items should be object"