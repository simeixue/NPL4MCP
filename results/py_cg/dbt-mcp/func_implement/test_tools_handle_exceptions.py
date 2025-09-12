# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_tools_handle_exceptions
# lines: 288-301
def test_tools_handle_exceptions(mock_get_prompt, mock_config):
    mock_get_prompt.return_value = "Test prompt"
    mock_admin_client = Mock()
    mock_admin_client.list_jobs.side_effect = Exception("API Error")

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    list_jobs_tool = tool_definitions[0].fn  # First tool is list_jobs

    result = list_jobs_tool()

    assert isinstance(result, str)
    assert "API Error" in result