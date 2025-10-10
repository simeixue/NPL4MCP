# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.password
# lines: 87-89
    def password(self) -> str:
        """Get the ClickHouse password."""
        return os.environ["CLICKHOUSE_PASSWORD"]