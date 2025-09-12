# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.get_job_run_artifact
# lines: 219-241
    def get_job_run_artifact(
        self,
        account_id: int,
        run_id: int,
        artifact_path: str,
        step: int | None = None,
    ) -> Any:
        """Get a specific job run artifact."""
        params = {}
        if step:
            params["step"] = step

        get_artifact_header = {
            "Accept": "*/*",
        } | self.config.headers

        response = requests.get(
            f"{self.config.url}/api/v2/accounts/{account_id}/runs/{run_id}/artifacts/{artifact_path}",
            headers=get_artifact_header,
            params=params,
        )
        response.raise_for_status()
        return response.text