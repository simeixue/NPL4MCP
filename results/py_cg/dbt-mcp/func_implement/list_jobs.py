# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.list_jobs
# lines: 41-106
    def list_jobs(self, account_id: int, **params) -> list[dict[str, Any]]:
        """List jobs for an account."""
        result = self._make_request(
            "GET",
            f"/api/v2/accounts/{account_id}/jobs/?include_related=['most_recent_run','most_recent_completed_run']",
            params=params,
        )
        data = result.get("data", [])

        # we filter the data to the most relevant fields
        # the rest of the fields can be retrieved with the get_job tool
        filtered_data = [
            {
                "id": job.get("id"),
                "name": job.get("name"),
                "description": job.get("description"),
                "dbt_version": job.get("dbt_version"),
                "job_type": job.get("job_type"),
                "triggers": job.get("triggers"),
                "most_recent_run_id": job.get("most_recent_run").get("id")
                if job.get("most_recent_run")
                else None,
                "most_recent_run_status": job.get("most_recent_run").get(
                    "status_humanized"
                )
                if job.get("most_recent_run")
                else None,
                "most_recent_run_started_at": job.get("most_recent_run").get(
                    "started_at"
                )
                if job.get("most_recent_run")
                else None,
                "most_recent_run_finished_at": job.get("most_recent_run").get(
                    "finished_at"
                )
                if job.get("most_recent_run")
                else None,
                "most_recent_completed_run_id": job.get(
                    "most_recent_completed_run"
                ).get("id")
                if job.get("most_recent_completed_run")
                else None,
                "most_recent_completed_run_status": job.get(
                    "most_recent_completed_run"
                ).get("status_humanized")
                if job.get("most_recent_completed_run")
                else None,
                "most_recent_completed_run_started_at": job.get(
                    "most_recent_completed_run"
                ).get("started_at")
                if job.get("most_recent_completed_run")
                else None,
                "most_recent_completed_run_finished_at": job.get(
                    "most_recent_completed_run"
                ).get("finished_at")
                if job.get("most_recent_completed_run")
                else None,
                "schedule": job.get("schedule").get("cron")
                if job.get("schedule")
                else None,
                "next_run": job.get("next_run"),
            }
            for job in data
        ]

        return filtered_data