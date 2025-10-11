# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.host
# lines: 56-58
    def host(self) -> str:
        """Get the Hydrolix host."""
        return os.environ["HYDROLIX_HOST"]