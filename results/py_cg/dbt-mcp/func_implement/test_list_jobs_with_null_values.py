# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_list_jobs_with_null_values
# lines: 126-151
def test_list_jobs_with_null_values(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": [
            {
                "id": 1,
                "name": "test_job",
                "description": None,
                "dbt_version": "1.7.0",
                "job_type": "deploy",
                "triggers": {},
                "most_recent_run": None,
                "most_recent_completed_run": None,
                "schedule": None,
                "next_run": None,
            }
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.list_jobs(12345)

    assert len(result) == 1
    assert result[0]["most_recent_run_id"] is None
    assert result[0]["schedule"] is None