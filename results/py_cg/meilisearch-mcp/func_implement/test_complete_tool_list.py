# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPToolDiscovery.test_complete_tool_list
# lines: 230-268
    async def test_complete_tool_list(self, mcp_server):
        """Test that all expected tools are discoverable by MCP clients"""
        tools = await simulate_list_tools(mcp_server)
        tool_names = [tool.name for tool in tools]

        # Complete list of expected tools (26 total - includes 4 new chat tools)
        expected_tools = [
            "get-connection-settings",
            "update-connection-settings",
            "health-check",
            "get-version",
            "get-stats",
            "create-index",
            "list-indexes",
            "delete-index",
            "get-documents",
            "add-documents",
            "get-settings",
            "update-settings",
            "search",
            "get-task",
            "get-tasks",
            "cancel-tasks",
            "get-keys",
            "create-key",
            "delete-key",
            "get-health-status",
            "get-index-metrics",
            "get-system-info",
            # New chat tools added in v0.6.0
            "create-chat-completion",
            "get-chat-workspaces",
            "get-chat-workspace-settings",
            "update-chat-workspace-settings",
        ]

        assert len(tools) == len(expected_tools)
        for tool_name in expected_tools:
            assert tool_name in tool_names