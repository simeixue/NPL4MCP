# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_trigger_job_run_tool
# lines: 167-180
def test_trigger_job_run_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "Trigger job run prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    trigger_job_run_tool = tool_definitions[2].fn  # Third tool is trigger_job_run

    result = trigger_job_run_tool(job_id=1, cause="Manual trigger", git_branch="main")

    assert isinstance(result, dict)
    mock_admin_client.trigger_job_run.assert_called_once_with(
        12345, 1, "Manual trigger", git_branch="main"
    )