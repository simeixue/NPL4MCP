# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.get_job_run_artifact
# lines: 169-181
    def get_job_run_artifact(
        run_id: int, artifact_path: str, step: int | None = None
    ) -> Any | str:
        """Get a specific job run artifact."""
        try:
            return admin_client.get_job_run_artifact(
                admin_api_config.account_id, run_id, artifact_path, step
            )
        except Exception as e:
            logger.error(
                f"Error getting artifact {artifact_path} for run {run_id}: {e}"
            )
            return str(e)