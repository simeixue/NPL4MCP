# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_get_job_details
# lines: 155-168
def test_get_job_details(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {"data": {"id": 1, "name": "test_job"}}
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.get_job_details(12345, 1)

    assert result == {"id": 1, "name": "test_job"}
    mock_request.assert_called_once_with(
        "GET",
        "https://cloud.getdbt.com/api/v2/accounts/12345/jobs/1/?include_related=['most_recent_run','most_recent_completed_run']",
        headers=client.headers,
    )