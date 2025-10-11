# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.TransportType.values
# lines: 21-23
    def values(cls) -> list[str]:
        """Get all valid transport values."""
        return [transport.value for transport in cls]