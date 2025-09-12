# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.retry_job_run
# lines: 195-200
    def retry_job_run(self, account_id: int, run_id: int) -> dict[str, Any]:
        """Retry a failed job run."""
        result = self._make_request(
            "POST", f"/api/v2/accounts/{account_id}/runs/{run_id}/retry/"
        )
        return result.get("data", {})