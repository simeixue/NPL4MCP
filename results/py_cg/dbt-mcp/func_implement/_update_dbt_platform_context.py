# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app.create_app._update_dbt_platform_context
# lines: 125-141
    def _update_dbt_platform_context(
        new_dbt_platform_context: DbtPlatformContext,
    ) -> DbtPlatformContext:
        existing_dbt_platform_context = DbtPlatformContext.from_file(config_location)
        if existing_dbt_platform_context is None:
            existing_dbt_platform_context = DbtPlatformContext()
        next_dbt_platform_context = existing_dbt_platform_context.override(
            new_dbt_platform_context
        )
        app.state.dbt_platform_context = next_dbt_platform_context
        config_location.write_text(
            data=yaml.safe_dump(
                next_dbt_platform_context.model_dump(),
                sort_keys=True,
            )
        )
        return next_dbt_platform_context