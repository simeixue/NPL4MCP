# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.create_config
# lines: 325-458
def create_config(settings: DbtMcpSettings) -> Config:
    # Set default warn error options if not provided
    if settings.dbt_warn_error_options is None:
        warn_error_options = '{"error": ["NoNodesForSelectionCriteria"]}'
        os.environ["DBT_WARN_ERROR_OPTIONS"] = warn_error_options

    errors = validate_settings(settings)
    if errors:
        raise ValueError("Errors found in configuration:\n\n" + "\n".join(errors))

    # Build configurations
    sql_config = None
    if (
        not settings.actual_disable_sql
        and settings.dbt_user_id
        and settings.dbt_token
        and settings.dbt_dev_env_id
        and settings.actual_prod_environment_id
        and settings.actual_host
    ):
        sql_config = SqlConfig(
            host_prefix=settings.actual_host_prefix,
            user_id=settings.dbt_user_id,
            token=settings.dbt_token,
            dev_environment_id=settings.dbt_dev_env_id,
            prod_environment_id=settings.actual_prod_environment_id,
            host=settings.actual_host,
        )

    # For admin API tools, we need token, host, and account_id
    admin_api_config = None
    if (
        not settings.disable_admin_api
        and settings.dbt_token
        and settings.actual_host
        and settings.dbt_account_id
    ):
        if settings.actual_host_prefix:
            url = f"https://{settings.actual_host_prefix}.{settings.actual_host}"
        else:
            url = f"https://{settings.actual_host}"
        admin_api_config = AdminApiConfig(
            url=url,
            headers={"Authorization": f"Bearer {settings.dbt_token}"},
            account_id=settings.dbt_account_id,
            prod_environment_id=settings.actual_prod_environment_id,
        )

    dbt_cli_config = None
    if not settings.disable_dbt_cli and settings.dbt_project_dir and settings.dbt_path:
        binary_type = detect_binary_type(settings.dbt_path)
        dbt_cli_config = DbtCliConfig(
            project_dir=settings.dbt_project_dir,
            dbt_path=settings.dbt_path,
            dbt_cli_timeout=settings.dbt_cli_timeout,
            binary_type=binary_type,
        )

    discovery_config = None
    if (
        not settings.disable_discovery
        and settings.actual_host
        and settings.actual_prod_environment_id
        and settings.dbt_token
    ):
        if settings.actual_host_prefix:
            url = f"https://{settings.actual_host_prefix}.metadata.{settings.actual_host}/graphql"
        else:
            url = f"https://metadata.{settings.actual_host}/graphql"
        discovery_config = DiscoveryConfig(
            url=url,
            headers={
                "Authorization": f"Bearer {settings.dbt_token}",
                "Content-Type": "application/json",
            },
            environment_id=settings.actual_prod_environment_id,
        )

    semantic_layer_config = None
    if (
        not settings.disable_semantic_layer
        and settings.actual_host
        and settings.actual_prod_environment_id
        and settings.dbt_token
    ):
        is_local = settings.actual_host and settings.actual_host.startswith("localhost")
        if is_local:
            host = settings.actual_host
        elif settings.actual_host_prefix:
            host = (
                f"{settings.actual_host_prefix}.semantic-layer.{settings.actual_host}"
            )
        else:
            host = f"semantic-layer.{settings.actual_host}"
        assert host is not None

        semantic_layer_config = SemanticLayerConfig(
            url=f"http://{host}" if is_local else f"https://{host}" + "/api/graphql",
            host=host,
            prod_environment_id=settings.actual_prod_environment_id,
            service_token=settings.dbt_token,
            headers={
                "Authorization": f"Bearer {settings.dbt_token}",
                "x-dbt-partner-source": "dbt-mcp",
            },
        )

    # Load local user ID from dbt profile
    local_user_id = None
    try:
        home = os.environ.get("HOME")
        user_path = Path(f"{home}/.dbt/.user.yml")
        if home and user_path.exists():
            with open(user_path) as f:
                local_user_id = yaml.safe_load(f).get("id")
    except Exception:
        pass

    return Config(
        tracking_config=TrackingConfig(
            host=settings.actual_host,
            host_prefix=settings.actual_host_prefix,
            prod_environment_id=settings.actual_prod_environment_id,
            dev_environment_id=settings.dbt_dev_env_id,
            dbt_cloud_user_id=settings.dbt_user_id,
            local_user_id=local_user_id,
        ),
        sql_config=sql_config,
        dbt_cli_config=dbt_cli_config,
        discovery_config=discovery_config,
        semantic_layer_config=semantic_layer_config,
        admin_api_config=admin_api_config,
        disable_tools=settings.disable_tools or [],
    )