# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.mock_admin_client
# lines: 51-95
def mock_admin_client():
    client = Mock()
    client.list_jobs.return_value = [
        {
            "id": 1,
            "name": "test_job",
            "description": "Test job description",
            "dbt_version": "1.7.0",
            "job_type": "deploy",
            "triggers": {},
            "most_recent_run_id": 100,
            "most_recent_run_status": "success",
            "schedule": "0 9 * * *",
        }
    ]
    client.get_job_details.return_value = {"id": 1, "name": "test_job"}
    client.trigger_job_run.return_value = {"id": 200, "status": "queued"}
    client.list_jobs_runs.return_value = [
        {
            "id": 100,
            "status": 10,
            "status_humanized": "Success",
            "job_definition_id": 1,
            "started_at": "2024-01-01T00:00:00Z",
            "finished_at": "2024-01-01T00:05:00Z",
        }
    ]
    client.get_job_run_details.return_value = {
        "id": 100,
        "status": 10,
        "status_humanized": "Success",
    }
    client.cancel_job_run.return_value = {
        "id": 100,
        "status": 20,
        "status_humanized": "Cancelled",
    }
    client.retry_job_run.return_value = {
        "id": 101,
        "status": 1,
        "status_humanized": "Queued",
    }
    client.list_job_run_artifacts.return_value = ["manifest.json", "catalog.json"]
    client.get_job_run_artifact.return_value = {"nodes": {}}
    return client