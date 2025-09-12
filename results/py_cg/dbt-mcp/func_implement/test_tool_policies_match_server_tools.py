# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/tools/test_tool_policies.py
# module: tests.unit.tools.test_tool_policies
# qname: tests.unit.tools.test_tool_policies.test_tool_policies_match_server_tools
# lines: 11-36
async def test_tool_policies_match_server_tools():
    """Test that the ToolPolicy enum matches the tools registered in the server."""
    sql_tool_names = {"text_to_sql", "execute_sql"}

    with (
        default_env_vars_context(),
        patch(
            "dbt_mcp.config.config.detect_binary_type", return_value=BinaryType.DBT_CORE
        ),
    ):
        config = load_config()
        dbt_mcp = await create_dbt_mcp(config)

        # Get all tools from the server
        server_tools = await dbt_mcp.list_tools()
        # Manually adding SQL tools here because the server doesn't get them
        # in this unit test.
        server_tool_names = {tool.name for tool in server_tools} | sql_tool_names
        policy_names = {policy_name for policy_name in tool_policies}

        if server_tool_names != policy_names:
            raise ValueError(
                f"Tool name mismatch:\n"
                f"In server but not in enum: {server_tool_names - policy_names}\n"
                f"In enum but not in server: {policy_names - server_tool_names}"
            )