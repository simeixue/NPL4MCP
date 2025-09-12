# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/dbt_platform.py
# module: src.dbt_mcp.oauth.dbt_platform
# qname: src.dbt_mcp.oauth.dbt_platform.DbtPlatformAccount.host_prefix
# lines: 20-25
    def host_prefix(self) -> str | None:
        if self.static_subdomain:
            return self.static_subdomain
        if self.vanity_subdomain:
            return self.vanity_subdomain
        return None