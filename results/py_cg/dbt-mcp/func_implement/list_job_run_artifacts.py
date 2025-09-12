# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.list_job_run_artifacts
# lines: 202-217
    def list_job_run_artifacts(self, account_id: int, run_id: int) -> list[str]:
        """List artifacts for a job run."""
        result = self._make_request(
            "GET", f"/api/v2/accounts/{account_id}/runs/{run_id}/artifacts/"
        )
        data = result.get("data", [])

        # we remove the compiled and run artifacts, they are not very relevant and there are thousands of them, filling the context
        filtered_data = [
            artifact
            for artifact in data
            if (
                not artifact.startswith("compiled/") and not artifact.startswith("run/")
            )
        ]
        return filtered_data