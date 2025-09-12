# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/dbt_platform.py
# module: src.dbt_mcp.oauth.dbt_platform
# qname: src.dbt_mcp.oauth.dbt_platform.DbtPlatformContext.token
# lines: 66-71
    def token(self) -> str | None:
        return (
            self.decoded_access_token.access_token_response.access_token
            if self.decoded_access_token
            else None
        )