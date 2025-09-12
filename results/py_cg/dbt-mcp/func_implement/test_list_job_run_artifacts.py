# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_list_job_run_artifacts
# lines: 372-396
def test_list_job_run_artifacts(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": [
            "manifest.json",
            "catalog.json",
            "compiled/my_project/models/model.sql",
            "run/my_project/models/model.sql",
            "sources.json",
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.list_job_run_artifacts(12345, 100)

    # Should filter out compiled/ and run/ artifacts
    expected = ["manifest.json", "catalog.json", "sources.json"]
    assert result == expected

    mock_request.assert_called_once_with(
        "GET",
        "https://cloud.getdbt.com/api/v2/accounts/12345/runs/100/artifacts/",
        headers=client.headers,
    )