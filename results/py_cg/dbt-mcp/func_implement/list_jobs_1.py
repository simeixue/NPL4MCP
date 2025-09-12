# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.create_admin_api_tool_definitions.list_jobs
# lines: 44-66
    def list_jobs(
        # TODO: add support for project_id in the future
        # project_id: Optional[int] = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[dict[str, Any]] | str:
        """List jobs in an account."""
        try:
            params = {}
            # if project_id:
            #     params["project_id"] = project_id
            if admin_api_config.prod_environment_id:
                params["environment_id"] = admin_api_config.prod_environment_id
            if limit:
                params["limit"] = limit
            if offset:
                params["offset"] = offset
            return admin_client.list_jobs(admin_api_config.account_id, **params)
        except Exception as e:
            logger.error(
                f"Error listing jobs for account {admin_api_config.account_id}: {e}"
            )
            return str(e)