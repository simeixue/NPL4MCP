# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_trigger_job_run
# lines: 172-192
def test_trigger_job_run(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {"data": {"id": 200, "status": "queued"}}
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.trigger_job_run(
        12345, 1, "Manual trigger", git_branch="main", schema_override="test_schema"
    )

    assert result == {"id": 200, "status": "queued"}
    mock_request.assert_called_once_with(
        "POST",
        "https://cloud.getdbt.com/api/v2/accounts/12345/jobs/1/run/",
        headers=client.headers,
        json={
            "cause": "Manual trigger",
            "git_branch": "main",
            "schema_override": "test_schema",
        },
    )