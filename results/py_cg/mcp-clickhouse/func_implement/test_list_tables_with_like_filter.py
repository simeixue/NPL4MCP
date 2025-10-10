# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_list_tables_with_like_filter
# lines: 144-161
async def test_list_tables_with_like_filter(mcp_server, setup_test_database):
    """Test the list_tables tool with LIKE filter."""
    test_db, test_table, _ = setup_test_database

    async with Client(mcp_server) as client:
        # Test with LIKE filter
        result = await client.call_tool("list_tables", {"database": test_db, "like": "test_%"})

        tables_data = json.loads(result.content[0].text)

        # Handle both single dict and list of dicts
        if isinstance(tables_data, dict):
            tables = [tables_data]
        else:
            tables = tables_data

        assert len(tables) == 1
        assert tables[0]["name"] == test_table