# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_cancel_job_run
# lines: 338-351
def test_cancel_job_run(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {"data": {"id": 100, "status": "cancelled"}}
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.cancel_job_run(12345, 100)

    assert result == {"id": 100, "status": "cancelled"}
    mock_request.assert_called_once_with(
        "POST",
        "https://cloud.getdbt.com/api/v2/accounts/12345/runs/100/cancel/",
        headers=client.headers,
    )