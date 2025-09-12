# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.get_job_run_details
# lines: 167-186
    def get_job_run_details(
        self, account_id: int, run_id: int, debug: bool = False
    ) -> dict[str, Any]:
        """Get details for a specific job run."""

        # we add this for individual runs but not all of them
        incl = "?include_related=['run_steps']"
        if debug:
            incl = "?include_related=['run_steps','debug_logs']"
        result = self._make_request(
            "GET", f"/api/v2/accounts/{account_id}/runs/{run_id}/{incl}"
        )
        data = result.get("data", {})

        # we remove the truncated debug logs, they are not very relevant
        # if needed, in debug mode, we get the full debug logs which will be more relevant
        for step in data.get("run_steps", []):
            step.pop("truncated_debug_logs", None)

        return data