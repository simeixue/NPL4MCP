# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.list_jobs_runs
# lines: 126-165
    def list_jobs_runs(self, account_id: int, **params) -> list[dict[str, Any]]:
        """List runs for an account."""
        extra_info = "?include_related=['job']"
        result = self._make_request(
            "GET", f"/api/v2/accounts/{account_id}/runs/{extra_info}", params=params
        )

        data = result.get("data", [])

        # we remove less relevant fields from the data we get to avoid filling the context with too much data
        for run in data:
            run["job_name"] = run.get("job", {}).get("name", "")
            run["job_steps"] = run.get("job", {}).get("execute_step", "")
            run.pop("job", None)
            run.pop("account_id", None)
            run.pop("environment_id", None)
            run.pop("blocked_by", None)
            run.pop("used_repo_cache", None)
            run.pop("audit", None)
            run.pop("created_at_humanized", None)
            run.pop("duration_humanized", None)
            run.pop("finished_at_humanized", None)
            run.pop("queued_duration_humanized", None)
            run.pop("run_duration_humanized", None)
            run.pop("artifacts_saved", None)
            run.pop("artifact_s3_path", None)
            run.pop("has_docs_generated", None)
            run.pop("has_sources_generated", None)
            run.pop("notifications_sent", None)
            run.pop("executed_by_thread_id", None)
            run.pop("updated_at", None)
            run.pop("dequeued_at", None)
            run.pop("last_checked_at", None)
            run.pop("last_heartbeat_at", None)
            run.pop("trigger", None)
            run.pop("run_steps", None)
            run.pop("deprecation", None)
            run.pop("environment", None)

        return data