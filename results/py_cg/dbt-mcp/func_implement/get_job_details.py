# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.get_job_details
# lines: 108-114
    def get_job_details(self, account_id: int, job_id: int) -> dict[str, Any]:
        """Get details for a specific job."""
        result = self._make_request(
            "GET",
            f"/api/v2/accounts/{account_id}/jobs/{job_id}/?include_related=['most_recent_run','most_recent_completed_run']",
        )
        return result.get("data", {})