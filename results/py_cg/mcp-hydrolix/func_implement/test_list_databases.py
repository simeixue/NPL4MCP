# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_list_databases
# lines: 91-105
async def test_list_databases(mcp_server, setup_test_database):
    """Test the list_databases tool."""
    test_db, _, _ = setup_test_database

    async with Client(mcp_server) as client:
        result = await client.call_tool("list_databases", {})

        # The result should be a list containing at least one item
        assert len(result) >= 1
        assert isinstance(result[0].text, str)

        # Parse the result text (it's a JSON list of database names)
        databases = json.loads(result[0].text)
        assert test_db in databases
        assert "system" in databases  # System database should always exist