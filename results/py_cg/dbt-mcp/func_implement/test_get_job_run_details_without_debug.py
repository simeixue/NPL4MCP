# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_get_job_run_details_without_debug
# lines: 286-310
def test_get_job_run_details_without_debug(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": {
            "id": 100,
            "status": 10,
            "run_steps": [
                {"id": 1, "name": "dbt run", "truncated_debug_logs": "log data"}
            ],
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.get_job_run_details(12345, 100, debug=False)

    assert result["id"] == 100
    # Verify truncated_debug_logs are removed
    assert "truncated_debug_logs" not in result["run_steps"][0]

    mock_request.assert_called_once_with(
        "GET",
        "https://cloud.getdbt.com/api/v2/accounts/12345/runs/100/?include_related=['run_steps']",
        headers=client.headers,
    )