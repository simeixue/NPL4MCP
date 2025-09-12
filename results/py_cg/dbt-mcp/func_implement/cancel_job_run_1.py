# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.cancel_job_run
# lines: 143-149
    def cancel_job_run(run_id: int) -> dict[str, Any] | str:
        """Cancel a job run."""
        try:
            return admin_client.cancel_job_run(admin_api_config.account_id, run_id)
        except Exception as e:
            logger.error(f"Error cancelling run {run_id}: {e}")
            return str(e)