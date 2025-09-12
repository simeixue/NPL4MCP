# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_list_jobs_runs_tool
# lines: 184-197
def test_list_jobs_runs_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "List runs prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    list_jobs_runs_tool = tool_definitions[3].fn  # Fourth tool is list_jobs_runs

    result = list_jobs_runs_tool(job_id=1, status=JobRunStatus.SUCCESS, limit=5)

    assert isinstance(result, list)
    mock_admin_client.list_jobs_runs.assert_called_once_with(
        12345, job_definition_id=1, status=10, limit=5
    )