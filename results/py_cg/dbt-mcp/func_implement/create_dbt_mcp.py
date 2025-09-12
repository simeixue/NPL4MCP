# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/mcp/server.py
# module: src.dbt_mcp.mcp.server
# qname: src.dbt_mcp.mcp.server.create_dbt_mcp
# lines: 103-131
async def create_dbt_mcp(config: Config) -> DbtMCP:
    dbt_mcp = DbtMCP(
        config=config,
        usage_tracker=UsageTracker(),
        name="dbt",
        lifespan=app_lifespan,
    )

    if config.semantic_layer_config:
        logger.info("Registering semantic layer tools")
        register_sl_tools(dbt_mcp, config.semantic_layer_config, config.disable_tools)

    if config.discovery_config:
        logger.info("Registering discovery tools")
        register_discovery_tools(dbt_mcp, config.discovery_config, config.disable_tools)

    if config.dbt_cli_config:
        logger.info("Registering dbt cli tools")
        register_dbt_cli_tools(dbt_mcp, config.dbt_cli_config, config.disable_tools)

    if config.admin_api_config:
        logger.info("Registering dbt admin API tools")
        register_admin_api_tools(dbt_mcp, config.admin_api_config, config.disable_tools)

    if config.sql_config:
        logger.info("Registering SQL tools")
        await register_sql_tools(dbt_mcp, config.sql_config, config.disable_tools)

    return dbt_mcp