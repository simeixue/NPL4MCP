# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.trigger_job_run
# lines: 76-97
    def trigger_job_run(
        job_id: int,
        cause: str = "Triggered by dbt MCP",
        git_branch: str | None = None,
        git_sha: str | None = None,
        schema_override: str | None = None,
    ) -> dict[str, Any] | str:
        """Trigger a job run."""
        try:
            kwargs = {}
            if git_branch:
                kwargs["git_branch"] = git_branch
            if git_sha:
                kwargs["git_sha"] = git_sha
            if schema_override:
                kwargs["schema_override"] = schema_override
            return admin_client.trigger_job_run(
                admin_api_config.account_id, job_id, cause, **kwargs
            )
        except Exception as e:
            logger.error(f"Error triggering job {job_id}: {e}")
            return str(e)