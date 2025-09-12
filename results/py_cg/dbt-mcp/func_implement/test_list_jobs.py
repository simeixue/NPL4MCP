# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_list_jobs
# lines: 78-122
def test_list_jobs(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": [
            {
                "id": 1,
                "name": "test_job",
                "description": "Test description",
                "dbt_version": "1.7.0",
                "job_type": "deploy",
                "triggers": {"github_webhook": True},
                "most_recent_run": {
                    "id": 100,
                    "status_humanized": "Success",
                    "started_at": "2024-01-01T00:00:00Z",
                    "finished_at": "2024-01-01T00:05:00Z",
                },
                "most_recent_completed_run": {
                    "id": 99,
                    "status_humanized": "Success",
                    "started_at": "2024-01-01T00:00:00Z",
                    "finished_at": "2024-01-01T00:04:00Z",
                },
                "schedule": {"cron": "0 9 * * *"},
                "next_run": "2024-01-02T09:00:00Z",
            }
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.list_jobs(12345, project_id=1, limit=10)

    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["name"] == "test_job"
    assert result[0]["most_recent_run_id"] == 100
    assert result[0]["schedule"] == "0 9 * * *"

    mock_request.assert_called_once_with(
        "GET",
        "https://cloud.getdbt.com/api/v2/accounts/12345/jobs/?include_related=['most_recent_run','most_recent_completed_run']",
        headers=client.headers,
        params={"project_id": 1, "limit": 10},
    )