# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue27OpenAISchemaCompatibility.test_all_schemas_have_additional_properties_false
# lines: 625-637
    async def test_all_schemas_have_additional_properties_false(self, mcp_server):
        """Test that all tool schemas include additionalProperties: false for OpenAI compatibility (issue #27)"""
        tools = await simulate_list_tools(mcp_server)

        for tool in tools:
            schema = tool.inputSchema
            assert schema["type"] == "object"
            assert (
                "additionalProperties" in schema
            ), f"Tool '{tool.name}' missing additionalProperties"
            assert (
                schema["additionalProperties"] is False
            ), f"Tool '{tool.name}' additionalProperties should be false"