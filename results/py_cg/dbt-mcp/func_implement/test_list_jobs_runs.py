# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_list_jobs_runs
# lines: 196-282
def test_list_jobs_runs(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": [
            {
                "id": 100,
                "status": 10,
                "status_humanized": "Success",
                "job": {"name": "test_job", "execute_step": ["dbt run"]},
                "started_at": "2024-01-01T00:00:00Z",
                "finished_at": "2024-01-01T00:05:00Z",
                # Fields that should be removed
                "account_id": 12345,
                "environment_id": 1,
                "blocked_by": None,
                "used_repo_cache": True,
                "audit": {},
                "created_at_humanized": "1 hour ago",
                "duration_humanized": "5 minutes",
                "finished_at_humanized": "1 hour ago",
                "queued_duration_humanized": "10 seconds",
                "run_duration_humanized": "4 minutes 50 seconds",
                "artifacts_saved": True,
                "artifact_s3_path": "s3://bucket/path",
                "has_docs_generated": True,
                "has_sources_generated": False,
                "notifications_sent": True,
                "executed_by_thread_id": "thread123",
                "updated_at": "2024-01-01T00:05:00Z",
                "dequeued_at": "2024-01-01T00:00:30Z",
                "last_checked_at": "2024-01-01T00:04:00Z",
                "last_heartbeat_at": "2024-01-01T00:04:30Z",
                "trigger": {},
                "run_steps": [],
                "deprecation": {},
                "environment": {},
            }
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client.list_jobs_runs(12345, job_definition_id=1, status="success")

    assert len(result) == 1
    run = result[0]
    assert run["id"] == 100
    assert run["job_name"] == "test_job"
    assert run["job_steps"] == ["dbt run"]

    # Verify removed fields are not present
    removed_fields = [
        "job",
        "account_id",
        "environment_id",
        "blocked_by",
        "used_repo_cache",
        "audit",
        "created_at_humanized",
        "duration_humanized",
        "finished_at_humanized",
        "queued_duration_humanized",
        "run_duration_humanized",
        "artifacts_saved",
        "artifact_s3_path",
        "has_docs_generated",
        "has_sources_generated",
        "notifications_sent",
        "executed_by_thread_id",
        "updated_at",
        "dequeued_at",
        "last_checked_at",
        "last_heartbeat_at",
        "trigger",
        "run_steps",
        "deprecation",
        "environment",
    ]
    for field in removed_fields:
        assert field not in run

    mock_request.assert_called_once_with(
        "GET",
        "https://cloud.getdbt.com/api/v2/accounts/12345/runs/?include_related=['job']",
        headers=client.headers,
        params={"job_definition_id": 1, "status": "success"},
    )