# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.get_job_details
# lines: 68-74
    def get_job_details(job_id: int) -> dict[str, Any] | str:
        """Get details for a specific job."""
        try:
            return admin_client.get_job_details(admin_api_config.account_id, job_id)
        except Exception as e:
            logger.error(f"Error getting job {job_id}: {e}")
            return str(e)