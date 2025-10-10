# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.enabled
# lines: 58-63
    def enabled(self) -> bool:
        """Get whether ClickHouse server is enabled.

        Default: True
        """
        return os.getenv("CLICKHOUSE_ENABLED", "true").lower() == "true"