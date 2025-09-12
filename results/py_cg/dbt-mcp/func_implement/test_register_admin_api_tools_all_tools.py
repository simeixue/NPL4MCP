# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_register_admin_api_tools_all_tools
# lines: 100-112
def test_register_admin_api_tools_all_tools(
    mock_get_prompt, mock_register_tools, mock_config, mock_fastmcp
):
    mock_get_prompt.return_value = "Test prompt"
    fastmcp, tools = mock_fastmcp

    register_admin_api_tools(fastmcp, mock_config.admin_api_config, [])

    # Should call register_tools with 9 tool definitions
    mock_register_tools.assert_called_once()
    args, kwargs = mock_register_tools.call_args
    tool_definitions = args[1]  # Second argument is the tool definitions list
    assert len(tool_definitions) == 9