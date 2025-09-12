# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.get_dbt_platform_context
# lines: 265-284
def get_dbt_platform_context(settings: DbtMcpSettings) -> DbtPlatformContext:
    # Some MCP hosts (Claude Desktop) tend to run multiple MCP servers instances.
    # We need to lock so that only one can run the oauth flow.
    dbt_user_dir = _get_dbt_user_dir(dbt_profiles_dir=settings.dbt_profiles_dir)
    with FileLock(dbt_user_dir / "mcp.lock"):
        config_location = dbt_user_dir / "mcp.yml"
        if config_location.exists() and (
            dbt_ctx := DbtPlatformContext.from_file(config_location)
        ):
            return dbt_ctx
        config_location.parent.mkdir(parents=True, exist_ok=True)
        config_location.touch()
        # Find an available port for the local OAuth redirect server
        selected_port = _find_available_port(start_port=OAUTH_REDIRECT_STARTING_PORT)
        return login(
            dbt_platform_url=f"https://{settings.actual_host}",
            port=selected_port,
            client_id=OAUTH_CLIENT_ID,
            config_location=config_location,
        )