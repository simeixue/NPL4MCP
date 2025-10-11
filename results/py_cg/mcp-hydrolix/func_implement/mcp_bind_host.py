# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.mcp_bind_host
# lines: 154-160
    def mcp_bind_host(self) -> str:
        """Get the host to bind the MCP server to.

        Only used when transport is "http" or "sse".
        Default: "127.0.0.1"
        """
        return os.getenv("HYDROLIX_MCP_BIND_HOST", "127.0.0.1")