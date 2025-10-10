# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.host
# lines: 66-68
    def host(self) -> str:
        """Get the ClickHouse host."""
        return os.environ["CLICKHOUSE_HOST"]