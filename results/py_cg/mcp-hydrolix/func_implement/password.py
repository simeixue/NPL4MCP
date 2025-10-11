# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.password
# lines: 99-103
    def password(self) -> str:
        """Get the Hydrolix password."""
        if "HYDROLIX_PASSWORD" in os.environ:
            return os.environ["HYDROLIX_PASSWORD"]
        return None