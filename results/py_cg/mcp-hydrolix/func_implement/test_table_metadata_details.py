# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_table_metadata_details
# lines: 283-318
async def test_table_metadata_details(mcp_server, setup_test_database):
    """Test that table metadata is correctly retrieved."""
    test_db, test_table, _ = setup_test_database

    async with Client(mcp_server) as client:
        result = await client.call_tool("list_tables", {"database": test_db})
        tables = json.loads(result[0].text)

        # Find our test table
        test_table_info = next(t for t in tables if t["name"] == test_table)

        # Check table comment
        assert test_table_info["comment"] == "Test table for MCP server testing"

        # Check engine info
        assert test_table_info["engine"] == "MergeTree"
        assert "MergeTree" in test_table_info["engine_full"]

        # Check row count
        assert test_table_info["total_rows"] == 4

        # Check columns and their comments
        columns_by_name = {col["name"]: col for col in test_table_info["columns"]}

        assert columns_by_name["id"]["comment"] == "Primary identifier"
        assert columns_by_name["id"]["column_type"] == "UInt32"

        assert columns_by_name["name"]["comment"] == "User name field"
        assert columns_by_name["name"]["column_type"] == "String"

        assert columns_by_name["age"]["comment"] == "User age"
        assert columns_by_name["age"]["column_type"] == "UInt8"

        assert columns_by_name["created_at"]["comment"] == "Record creation timestamp"
        assert columns_by_name["created_at"]["column_type"] == "DateTime"
        assert columns_by_name["created_at"]["default_expression"] == "now()"