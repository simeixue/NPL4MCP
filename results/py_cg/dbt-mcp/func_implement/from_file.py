# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/dbt_platform.py
# module: src.dbt_mcp.oauth.dbt_platform
# qname: src.dbt_mcp.oauth.dbt_platform.DbtPlatformContext.from_file
# lines: 59-63
    def from_file(cls, config_location: Path) -> DbtPlatformContext | None:
        try:
            return cls(**yaml.safe_load(config_location.read_text()))
        except Exception:
            return None