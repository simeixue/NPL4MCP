# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.get_job_run_details
# lines: 127-141
    def get_job_run_details(
        run_id: int,
        debug: bool = Field(
            default=False,
            description="Set to True only if the person is explicitely asking for debug level logs. Otherwise, do not set if just the logs are asked.",
        ),
    ) -> dict[str, Any] | str:
        """Get details for a specific job run."""
        try:
            return admin_client.get_job_run_details(
                admin_api_config.account_id, run_id, debug=debug
            )
        except Exception as e:
            logger.error(f"Error getting run {run_id}: {e}")
            return str(e)