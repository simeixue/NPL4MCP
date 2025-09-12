# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.load_config
# lines: 287-322
def load_config() -> Config:
    # Load settings from environment variables using pydantic_settings
    settings = DbtMcpSettings()  # type: ignore[call-arg]
    dbt_platform_errors = validate_dbt_platform_settings(settings)
    # Oauth is exerimental but secure, so you shouldn't use it,
    # but there are no security concerns if you do.
    enable_oauth = os.environ.get("ENABLE_EXPERIMENAL_SECURE_OAUTH") == "true"
    if enable_oauth and dbt_platform_errors:
        actual_host = settings.actual_host
        if not actual_host:
            raise ValueError("DBT_HOST is a required environment variable")
        dbt_platform_context = get_dbt_platform_context(settings)

        # Override settings with settings attained from login or mcp.yml
        settings.dbt_user_id = dbt_platform_context.user_id
        settings.dbt_dev_env_id = (
            dbt_platform_context.dev_environment.id
            if dbt_platform_context.dev_environment
            else None
        )
        settings.dbt_prod_env_id = (
            dbt_platform_context.prod_environment.id
            if dbt_platform_context.prod_environment
            else None
        )
        settings.dbt_token = dbt_platform_context.token
        settings.host_prefix = dbt_platform_context.host_prefix
        host_prefix_with_period = f"{dbt_platform_context.host_prefix}."
        if not actual_host.startswith(host_prefix_with_period):
            raise ValueError(
                f"The DBT_HOST environment variable is expected to start with the {dbt_platform_context.host_prefix} custom subdomain."
            )
        # We have to remove the custom subdomain prefix
        # so that the metadata and semantic-layer URLs can be constructed correctly.
        settings.dbt_host = actual_host.removeprefix(host_prefix_with_period)
    return create_config(settings)