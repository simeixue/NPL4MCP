# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.username
# lines: 82-84
    def username(self) -> str:
        """Get the ClickHouse username."""
        return os.environ["CLICKHOUSE_USER"]