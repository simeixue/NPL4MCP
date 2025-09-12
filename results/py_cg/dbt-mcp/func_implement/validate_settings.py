# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.validate_settings
# lines: 193-197
def validate_settings(settings: DbtMcpSettings) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_dbt_platform_settings(settings))
    errors.extend(validate_dbt_cli_settings(settings))
    return errors