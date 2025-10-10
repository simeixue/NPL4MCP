# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_concurrent_queries
# lines: 340-365
async def test_concurrent_queries(mcp_server, setup_test_database):
    """Test running multiple queries concurrently."""
    test_db, test_table, test_table2 = setup_test_database

    async with Client(mcp_server) as client:
        # Run multiple queries concurrently
        queries = [
            f"SELECT COUNT(*) FROM {test_db}.{test_table}",
            f"SELECT COUNT(*) FROM {test_db}.{test_table2}",
            f"SELECT MAX(id) FROM {test_db}.{test_table}",
            f"SELECT MIN(event_id) FROM {test_db}.{test_table2}",
        ]

        # Execute all queries concurrently
        results = await asyncio.gather(
            *[client.call_tool("run_select_query", {"query": query}) for query in queries]
        )

        # Verify all queries succeeded
        assert len(results) == 4

        # Check each result
        for i, result in enumerate(results):
            query_result = json.loads(result.content[0].text)
            assert "rows" in query_result
            assert len(query_result["rows"]) == 1