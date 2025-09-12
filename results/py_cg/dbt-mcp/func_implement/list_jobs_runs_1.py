# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.list_jobs_runs
# lines: 99-125
    def list_jobs_runs(
        job_id: int | None = None,
        status: JobRunStatus | None = None,
        limit: int | None = None,
        offset: int | None = None,
        order_by: str | None = None,
    ) -> list[dict[str, Any]] | str:
        """List runs in an account."""
        try:
            params: dict[str, Any] = {}
            if job_id:
                params["job_definition_id"] = job_id
            if status:
                status_id = STATUS_MAP[status]
                params["status"] = status_id
            if limit:
                params["limit"] = limit
            if offset:
                params["offset"] = offset
            if order_by:
                params["order_by"] = order_by
            return admin_client.list_jobs_runs(admin_api_config.account_id, **params)
        except Exception as e:
            logger.error(
                f"Error listing runs for account {admin_api_config.account_id}: {e}"
            )
            return str(e)