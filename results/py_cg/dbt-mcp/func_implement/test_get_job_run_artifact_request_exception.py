# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_get_job_run_artifact_request_exception
# lines: 455-459
def test_get_job_run_artifact_request_exception(mock_get, client):
    mock_get.side_effect = requests.exceptions.HTTPError("404 Not Found")

    with pytest.raises(requests.exceptions.HTTPError):
        client.get_job_run_artifact(12345, 100, "nonexistent.json")