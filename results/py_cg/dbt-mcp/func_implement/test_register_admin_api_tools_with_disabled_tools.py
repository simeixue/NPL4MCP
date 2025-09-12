# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_register_admin_api_tools_with_disabled_tools
# lines: 117-133
def test_register_admin_api_tools_with_disabled_tools(
    mock_get_prompt, mock_register_tools, mock_config, mock_fastmcp
):
    mock_get_prompt.return_value = "Test prompt"
    fastmcp, tools = mock_fastmcp

    disable_tools = ["list_jobs", "get_job", "trigger_job_run"]
    register_admin_api_tools(fastmcp, mock_config.admin_api_config, disable_tools)

    # Should still call register_tools with all 9 tool definitions
    # The exclude_tools parameter is passed to register_tools to handle filtering
    mock_register_tools.assert_called_once()
    args, kwargs = mock_register_tools.call_args
    tool_definitions = args[1]  # Second argument is the tool definitions list
    exclude_tools_arg = args[2]  # Third argument is exclude_tools
    assert len(tool_definitions) == 9
    assert exclude_tools_arg == disable_tools