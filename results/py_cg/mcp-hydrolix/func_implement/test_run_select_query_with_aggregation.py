# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_run_select_query_with_aggregation
# lines: 212-225
async def test_run_select_query_with_aggregation(mcp_server, setup_test_database):
    """Test running a SELECT query with aggregation."""
    test_db, test_table, _ = setup_test_database

    async with Client(mcp_server) as client:
        query = f"SELECT COUNT(*) as count, AVG(age) as avg_age FROM {test_db}.{test_table}"
        result = await client.call_tool("run_select_query", {"query": query})

        query_result = json.loads(result[0].text)

        assert query_result["columns"] == ["count", "avg_age"]
        assert len(query_result["rows"]) == 1
        assert query_result["rows"][0][0] == 4  # count
        assert query_result["rows"][0][1] == 29.5  # average age