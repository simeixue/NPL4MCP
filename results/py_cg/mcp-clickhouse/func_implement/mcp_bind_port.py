# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.mcp_bind_port
# lines: 157-163
    def mcp_bind_port(self) -> int:
        """Get the port to bind the MCP server to.

        Only used when transport is "http" or "sse".
        Default: 8000
        """
        return int(os.getenv("CLICKHOUSE_MCP_BIND_PORT", "8000"))