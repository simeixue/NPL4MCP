# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_list_tables_basic
# lines: 109-140
async def test_list_tables_basic(mcp_server, setup_test_database):
    """Test the list_tables tool without filters."""
    test_db, test_table, test_table2 = setup_test_database

    async with Client(mcp_server) as client:
        result = await client.call_tool("list_tables", {"database": test_db})

        assert len(result) >= 1
        tables = json.loads(result[0].text)

        # Should have exactly 2 tables
        assert len(tables) == 2

        # Get table names
        table_names = [table["name"] for table in tables]
        assert test_table in table_names
        assert test_table2 in table_names

        # Check table details
        for table in tables:
            assert table["database"] == test_db
            assert "columns" in table
            assert "total_rows" in table
            assert "engine" in table
            assert "comment" in table

            # Verify column information exists
            assert len(table["columns"]) > 0
            for column in table["columns"]:
                assert "name" in column
                assert "column_type" in column
                assert "comment" in column