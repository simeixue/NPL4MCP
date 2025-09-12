# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.trigger_job_run
# lines: 116-124
    def trigger_job_run(
        self, account_id: int, job_id: int, cause: str, **kwargs
    ) -> dict[str, Any]:
        """Trigger a job run."""
        data = {"cause": cause, **kwargs}
        result = self._make_request(
            "POST", f"/api/v2/accounts/{account_id}/jobs/{job_id}/run/", json=data
        )
        return result.get("data", {})