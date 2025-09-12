# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/dbt_platform.py
# module: src.dbt_mcp.oauth.dbt_platform
# qname: src.dbt_mcp.oauth.dbt_platform.DbtPlatformContext.override
# lines: 81-88
    def override(self, other: DbtPlatformContext) -> DbtPlatformContext:
        return DbtPlatformContext(
            dev_environment=other.dev_environment or self.dev_environment,
            prod_environment=other.prod_environment or self.prod_environment,
            decoded_access_token=other.decoded_access_token
            or self.decoded_access_token,
            host_prefix=other.host_prefix or self.host_prefix,
        )