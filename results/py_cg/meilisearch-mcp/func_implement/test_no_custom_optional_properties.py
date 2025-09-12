# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue27OpenAISchemaCompatibility.test_no_custom_optional_properties
# lines: 659-670
    async def test_no_custom_optional_properties(self, mcp_server):
        """Test that schemas don't use non-standard 'optional' property (issue #27)"""
        tools = await simulate_list_tools(mcp_server)

        for tool in tools:
            schema = tool.inputSchema
            properties = schema.get("properties", {})

            for prop_name, prop_schema in properties.items():
                assert (
                    "optional" not in prop_schema
                ), f"Tool '{tool.name}' property '{prop_name}' uses non-standard 'optional'"