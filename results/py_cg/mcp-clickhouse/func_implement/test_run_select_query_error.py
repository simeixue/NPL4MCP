# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_run_select_query_error
# lines: 253-265
async def test_run_select_query_error(mcp_server, setup_test_database):
    """Test running a SELECT query that results in an error."""
    test_db, _, _ = setup_test_database

    async with Client(mcp_server) as client:
        # Query non-existent table
        query = f"SELECT * FROM {test_db}.non_existent_table"

        # Should raise ToolError
        with pytest.raises(ToolError) as exc_info:
            await client.call_tool("run_select_query", {"query": query})

        assert "Query execution failed" in str(exc_info.value)