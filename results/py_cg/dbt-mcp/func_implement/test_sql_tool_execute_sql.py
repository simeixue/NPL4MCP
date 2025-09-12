# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/remote_tools/test_remote_tools.py
# module: tests.integration.remote_tools.test_remote_tools
# qname: tests.integration.remote_tools.test_remote_tools.test_sql_tool_execute_sql
# lines: 7-15
async def test_sql_tool_execute_sql():
    config = load_config()
    dbt_mcp = FastMCP("Test")
    await register_sql_tools(dbt_mcp, config.sql_config)
    tools = await dbt_mcp.list_tools()
    print(tools)
    result = await dbt_mcp.call_tool("execute_sql", {"sql": "SELECT 1"})
    assert len(result) == 1
    assert "1" in result[0].text