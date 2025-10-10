# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.secure
# lines: 97-102
    def secure(self) -> bool:
        """Get whether HTTPS is enabled.

        Default: True
        """
        return os.getenv("CLICKHOUSE_SECURE", "true").lower() == "true"