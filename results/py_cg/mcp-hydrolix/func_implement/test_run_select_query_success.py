# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_run_select_query_success
# lines: 186-208
async def test_run_select_query_success(mcp_server, setup_test_database):
    """Test running a successful SELECT query."""
    test_db, test_table, _ = setup_test_database

    async with Client(mcp_server) as client:
        query = f"SELECT id, name, age FROM {test_db}.{test_table} ORDER BY id"
        result = await client.call_tool("run_select_query", {"query": query})

        query_result = json.loads(result[0].text)

        # Check structure
        assert "columns" in query_result
        assert "rows" in query_result

        # Check columns
        assert query_result["columns"] == ["id", "name", "age"]

        # Check rows
        assert len(query_result["rows"]) == 4
        assert query_result["rows"][0] == [1, "Alice", 30]
        assert query_result["rows"][1] == [2, "Bob", 25]
        assert query_result["rows"][2] == [3, "Charlie", 35]
        assert query_result["rows"][3] == [4, "Diana", 28]