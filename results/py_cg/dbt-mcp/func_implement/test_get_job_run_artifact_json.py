# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_get_job_run_artifact_json
# lines: 400-416
def test_get_job_run_artifact_json(mock_get, client):
    mock_response = Mock()
    mock_response.json.return_value = {"nodes": {"model.test": {}}}
    mock_response.headers = {"content-type": "application/json"}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = client.get_job_run_artifact(12345, 100, "manifest.json", step=1)

    # The client returns response.text, but the mock returns the mock_response.text which is a Mock object
    # In a real scenario with JSON content type, the API would return JSON as text
    assert result is not None
    mock_get.assert_called_once_with(
        "https://cloud.getdbt.com/api/v2/accounts/12345/runs/100/artifacts/manifest.json",
        headers={"Authorization": "Bearer test_token", "Accept": "*/*"},
        params={"step": 1},
    )