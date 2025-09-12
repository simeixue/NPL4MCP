# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_get_job_run_artifact_tool
# lines: 267-284
def test_get_job_run_artifact_tool(mock_get_prompt, mock_config, mock_admin_client):
    mock_get_prompt.return_value = "Get run artifact prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )
    get_job_run_artifact_tool = tool_definitions[
        8
    ].fn  # Ninth tool is get_job_run_artifact

    result = get_job_run_artifact_tool(
        run_id=100, artifact_path="manifest.json", step=1
    )

    assert result is not None
    mock_admin_client.get_job_run_artifact.assert_called_once_with(
        12345, 100, "manifest.json", 1
    )