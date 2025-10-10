# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.connect_timeout
# lines: 113-118
    def connect_timeout(self) -> int:
        """Get the connection timeout in seconds.

        Default: 30
        """
        return int(os.getenv("CLICKHOUSE_CONNECT_TIMEOUT", "30"))