# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config._get_dbt_user_dir
# lines: 165-170
def _get_dbt_user_dir(dbt_profiles_dir: str | None = None) -> Path:
    # Respect DBT_PROFILES_DIR if set; otherwise default to ~/.dbt/mcp.yml
    if dbt_profiles_dir:
        return Path(dbt_profiles_dir).expanduser()
    else:
        return Path.home() / ".dbt"