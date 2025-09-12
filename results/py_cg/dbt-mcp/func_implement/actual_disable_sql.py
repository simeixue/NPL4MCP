# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.DbtMcpSettings.actual_disable_sql
# lines: 117-122
    def actual_disable_sql(self) -> bool:
        if self.disable_sql is not None:
            return self.disable_sql
        if self.disable_remote is not None:
            return self.disable_remote
        return True