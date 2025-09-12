# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPClientIntegration.test_tool_schema_validation
# lines: 195-210
    async def test_tool_schema_validation(self, mcp_server):
        """Test that tools have proper input schemas for MCP client validation"""
        tools = await simulate_list_tools(mcp_server)

        # Check specific tool schemas
        create_index_tool = next(tool for tool in tools if tool.name == "create-index")
        assert create_index_tool.inputSchema["type"] == "object"
        assert "uid" in create_index_tool.inputSchema["required"]
        assert "uid" in create_index_tool.inputSchema["properties"]
        assert create_index_tool.inputSchema["properties"]["uid"]["type"] == "string"

        search_tool = next(tool for tool in tools if tool.name == "search")
        assert search_tool.inputSchema["type"] == "object"
        assert "query" in search_tool.inputSchema["required"]
        assert "query" in search_tool.inputSchema["properties"]
        assert search_tool.inputSchema["properties"]["query"]["type"] == "string"