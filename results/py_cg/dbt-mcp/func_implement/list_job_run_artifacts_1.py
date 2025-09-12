# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.list_job_run_artifacts
# lines: 159-167
    def list_job_run_artifacts(run_id: int) -> list[str] | str:
        """List artifacts for a job run."""
        try:
            return admin_client.list_job_run_artifacts(
                admin_api_config.account_id, run_id
            )
        except Exception as e:
            logger.error(f"Error listing artifacts for run {run_id}: {e}")
            return str(e)