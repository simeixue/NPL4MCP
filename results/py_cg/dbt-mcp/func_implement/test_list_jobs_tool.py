# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_list_jobs_tool
# lines: 137-148
def test_list_jobs_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "List jobs prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    list_jobs_tool = tool_definitions[0].fn  # First tool is list_jobs

    result = list_jobs_tool(limit=10)

    assert isinstance(result, list)
    mock_admin_client.list_jobs.assert_called_once_with(12345, limit=10)