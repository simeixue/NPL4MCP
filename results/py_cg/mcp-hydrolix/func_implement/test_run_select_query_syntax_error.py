# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.test_run_select_query_syntax_error
# lines: 269-279
async def test_run_select_query_syntax_error(mcp_server):
    """Test running a SELECT query with syntax error."""
    async with Client(mcp_server) as client:
        # Invalid SQL syntax
        query = "SELECT FROM WHERE"

        # Should raise ToolError
        with pytest.raises(ToolError) as exc_info:
            await client.call_tool("run_select_query", {"query": query})

        assert "Query execution failed" in str(exc_info.value)