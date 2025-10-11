# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.connect_timeout
# lines: 119-124
    def connect_timeout(self) -> int:
        """Get the connection timeout in seconds.

        Default: 30
        """
        return int(os.getenv("HYDROLIX_CONNECT_TIMEOUT", "30"))