# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_run_select_query_with_join
# lines: 229-249
async def test_run_select_query_with_join(mcp_server, setup_test_database):
    """Test running a SELECT query with JOIN."""
    test_db, test_table, test_table2 = setup_test_database

    async with Client(mcp_server) as client:
        # Insert related data for join
        client_direct = create_clickhouse_client()
        client_direct.command(f"""
            INSERT INTO {test_db}.{test_table2} (event_id, event_type, timestamp) VALUES
            (2001, 'purchase', '2024-01-01 14:00:00')
        """)

        query = f"""
        SELECT
            COUNT(DISTINCT event_type) as event_types_count
        FROM {test_db}.{test_table2}
        """
        result = await client.call_tool("run_select_query", {"query": query})

        query_result = json.loads(result[0].text)
        assert query_result["rows"][0][0] == 3  # login, logout, purchase