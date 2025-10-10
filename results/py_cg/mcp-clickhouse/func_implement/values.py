# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.TransportType.values
# lines: 21-23
    def values(cls) -> list[str]:
        """Get all valid transport values."""
        return [transport.value for transport in cls]