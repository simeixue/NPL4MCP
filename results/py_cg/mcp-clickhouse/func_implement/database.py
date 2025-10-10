# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.database
# lines: 92-94
    def database(self) -> Optional[str]:
        """Get the default database name if set."""
        return os.getenv("CLICKHOUSE_DATABASE")