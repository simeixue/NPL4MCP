# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.retry_job_run
# lines: 151-157
    def retry_job_run(run_id: int) -> dict[str, Any] | str:
        """Retry a failed job run."""
        try:
            return admin_client.retry_job_run(admin_api_config.account_id, run_id)
        except Exception as e:
            logger.error(f"Error retrying run {run_id}: {e}")
            return str(e)