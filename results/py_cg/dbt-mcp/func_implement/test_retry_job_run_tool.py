# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_retry_job_run_tool
# lines: 235-246
def test_retry_job_run_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "Retry run prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    retry_job_run_tool = tool_definitions[6].fn  # Seventh tool is retry_job_run

    result = retry_job_run_tool(run_id=100)

    assert isinstance(result, dict)
    mock_admin_client.retry_job_run.assert_called_once_with(12345, 100)