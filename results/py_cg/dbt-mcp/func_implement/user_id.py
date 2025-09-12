# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/dbt_platform.py
# module: src.dbt_mcp.oauth.dbt_platform
# qname: src.dbt_mcp.oauth.dbt_platform.DbtPlatformContext.user_id
# lines: 74-79
    def user_id(self) -> int | None:
        return (
            int(self.decoded_access_token.decoded_claims["sub"])
            if self.decoded_access_token
            else None
        )