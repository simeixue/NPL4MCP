# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.TestMCPToolDiscovery.test_tool_categorization
# lines: 270-320
    async def test_tool_categorization(self, mcp_server):
        """Test that tools can be categorized for MCP client organization"""
        tools = await simulate_list_tools(mcp_server)

        # Categorize tools by functionality
        categories = {
            "connection": [t for t in tools if "connection" in t.name],
            "index": [
                t
                for t in tools
                if any(
                    word in t.name
                    for word in [
                        "index",
                        "create-index",
                        "list-indexes",
                        "delete-index",
                    ]
                )
            ],
            "document": [t for t in tools if "document" in t.name],
            "search": [t for t in tools if "search" in t.name],
            "task": [t for t in tools if "task" in t.name],
            "key": [t for t in tools if "key" in t.name],
            "monitoring": [
                t
                for t in tools
                if any(
                    word in t.name
                    for word in ["health", "stats", "version", "system", "metrics"]
                )
            ],
            "chat": [t for t in tools if "chat" in t.name],
        }

        # Verify minimum expected tools per category
        expected_counts = {
            "connection": 2,
            "index": 3,
            "document": 2,
            "search": 1,
            "task": 2,
            "key": 3,
            "monitoring": 4,
            "chat": 4,
        }

        for category, min_count in expected_counts.items():
            assert (
                len(categories[category]) >= min_count
            ), f"Category '{category}' has insufficient tools"