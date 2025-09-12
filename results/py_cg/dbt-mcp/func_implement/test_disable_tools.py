# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/tools/test_disable_tools.py
# module: tests.unit.tools.test_disable_tools
# qname: tests.unit.tools.test_disable_tools.test_disable_tools
# lines: 9-26
async def test_disable_tools():
    """Test that the ToolName enum matches the tools registered in the server."""
    disable_tools = {"get_mart_models", "list_metrics"}
    with (
        default_env_vars_context(
            override_env_vars={"DISABLE_TOOLS": ",".join(disable_tools)}
        ),
        patch(
            "dbt_mcp.config.config.detect_binary_type", return_value=BinaryType.DBT_CORE
        ),
    ):
        config = load_config()
        dbt_mcp = await create_dbt_mcp(config)

        # Get all tools from the server
        server_tools = await dbt_mcp.list_tools()
        server_tool_names = {tool.name for tool in server_tools}
        assert not disable_tools.intersection(server_tool_names)