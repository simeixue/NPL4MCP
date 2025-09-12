# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPClientIntegration.test_tool_discovery
# lines: 110-154
    async def test_tool_discovery(self, mcp_server):
        """Test that MCP client can discover all available tools from the server"""
        # Simulate MCP list_tools request
        tools = await simulate_list_tools(mcp_server)

        tool_names = [tool.name for tool in tools]

        # Verify basic structure
        assert isinstance(tools, list)
        assert len(tools) > 0

        # Check for essential tools
        essential_tools = [
            "get-connection-settings",
            "update-connection-settings",
            "health-check",
            "get-version",
            "get-stats",
            "create-index",
            "list-indexes",
            "get-documents",
            "add-documents",
            "search",
            "get-settings",
            "update-settings",
        ]

        for tool_name in essential_tools:
            assert tool_name in tool_names, f"Essential tool '{tool_name}' not found"

        # Verify tool structure
        for tool in tools:
            assert all(
                hasattr(tool, attr) for attr in ["name", "description", "inputSchema"]
            )
            assert all(
                isinstance(getattr(tool, attr), expected_type)
                for attr, expected_type in [
                    ("name", str),
                    ("description", str),
                    ("inputSchema", dict),
                ]
            )

        print(f"Discovered {len(tools)} tools: {tool_names}")