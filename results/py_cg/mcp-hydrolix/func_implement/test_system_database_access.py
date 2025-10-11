# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_system_database_access
# lines: 322-336
async def test_system_database_access(mcp_server):
    """Test that we can access system databases."""
    async with Client(mcp_server) as client:
        # List tables in system database
        result = await client.call_tool("list_tables", {"database": "system"})
        tables = json.loads(result[0].text)

        # System database should have many tables
        assert len(tables) > 10

        # Check for some common system tables
        table_names = [t["name"] for t in tables]
        assert "tables" in table_names
        assert "columns" in table_names
        assert "databases" in table_names