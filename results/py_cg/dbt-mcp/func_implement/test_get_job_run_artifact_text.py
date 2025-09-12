# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_get_job_run_artifact_text
# lines: 420-434
def test_get_job_run_artifact_text(mock_get, client):
    mock_response = Mock()
    mock_response.text = "LOG DATA"
    mock_response.headers = {"content-type": "text/plain"}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = client.get_job_run_artifact(12345, 100, "logs/dbt.log")

    assert result == "LOG DATA"
    mock_get.assert_called_once_with(
        "https://cloud.getdbt.com/api/v2/accounts/12345/runs/100/artifacts/logs/dbt.log",
        headers={"Authorization": "Bearer test_token", "Accept": "*/*"},
        params={},
    )