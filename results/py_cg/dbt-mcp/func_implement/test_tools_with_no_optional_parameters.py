# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.test_tools_with_no_optional_parameters
# lines: 305-335
def test_tools_with_no_optional_parameters(
    mock_get_prompt, mock_config, mock_admin_client
):
    mock_get_prompt.return_value = "Test prompt"

    tool_definitions = create_admin_api_tool_definitions(
        mock_admin_client, mock_config.admin_api_config
    )

    # Test list_jobs with no parameters
    list_jobs_tool = tool_definitions[0].fn
    result = list_jobs_tool()
    assert isinstance(result, list)
    mock_admin_client.list_jobs.assert_called_with(12345)

    # Test list_jobs_runs with no parameters
    list_jobs_runs_tool = tool_definitions[3].fn
    result = list_jobs_runs_tool()
    assert isinstance(result, list)
    mock_admin_client.list_jobs_runs.assert_called_with(12345)

    # Test get_job_run_details with default debug parameter
    get_job_run_details_tool = tool_definitions[4].fn
    result = get_job_run_details_tool(run_id=100)
    assert isinstance(result, dict)
    # The debug parameter should be a Field object with default False
    call_args = mock_admin_client.get_job_run_details.call_args
    assert call_args[0] == (12345, 100)
    debug_field = call_args[1]["debug"]
    # Check that it's a Field with the correct default
    assert hasattr(debug_field, "default") and debug_field.default is False