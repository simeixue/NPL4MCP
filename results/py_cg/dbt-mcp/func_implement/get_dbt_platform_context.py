# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app.create_app.get_dbt_platform_context
# lines: 224-226
    def get_dbt_platform_context() -> DbtPlatformContext:
        logger.info("Selected project received")
        return DbtPlatformContext.from_file(config_location) or DbtPlatformContext()