# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.DbtMcpSettings.actual_prod_environment_id
# lines: 113-114
    def actual_prod_environment_id(self) -> int | None:
        return self.dbt_prod_env_id or self.dbt_env_id