# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestIssue23DeleteIndexTool.test_delete_index_tool_discovery
# lines: 493-506
    async def test_delete_index_tool_discovery(self, mcp_server):
        """Test that delete-index tool is discoverable by MCP clients (issue #23)"""
        tools = await simulate_list_tools(mcp_server)
        tool_names = [tool.name for tool in tools]

        assert "delete-index" in tool_names

        # Find the delete-index tool and verify its schema
        delete_tool = next(tool for tool in tools if tool.name == "delete-index")
        assert delete_tool.description == "Delete a Meilisearch index"
        assert delete_tool.inputSchema["type"] == "object"
        assert "uid" in delete_tool.inputSchema["required"]
        assert "uid" in delete_tool.inputSchema["properties"]
        assert delete_tool.inputSchema["properties"]["uid"]["type"] == "string"