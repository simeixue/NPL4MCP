# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.username
# lines: 92-96
    def username(self) -> str:
        """Get the Hydrolix username."""
        if "HYDROLIX_USER" in os.environ:
            return os.environ["HYDROLIX_USER"]
        return None