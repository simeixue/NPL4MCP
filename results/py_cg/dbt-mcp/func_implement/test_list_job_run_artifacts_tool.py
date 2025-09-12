# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_list_job_run_artifacts_tool
# lines: 250-263
def test_list_job_run_artifacts_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "List run artifacts prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    list_job_run_artifacts_tool = tool_definitions[
        7
    ].fn  # Eighth tool is list_job_run_artifacts

    result = list_job_run_artifacts_tool(run_id=100)

    assert isinstance(result, list)
    mock_admin_client.list_job_run_artifacts.assert_called_once_with(12345, 100)