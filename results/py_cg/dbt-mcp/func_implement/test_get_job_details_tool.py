# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_get_job_details_tool
# lines: 152-163
def test_get_job_details_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "Get job prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    get_job_details_tool = tool_definitions[1].fn  # Second tool is get_job_details

    result = get_job_details_tool(job_id=1)

    assert isinstance(result, dict)
    mock_admin_client.get_job_details.assert_called_once_with(12345, 1)