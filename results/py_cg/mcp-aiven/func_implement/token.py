# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_env.py
# module: mcp_aiven.mcp_env
# qname: mcp_aiven.mcp_env.AivenConfig.token
# lines: 34-36
    def token(self) -> str:
        """Get the Aiven Token."""
        return os.getenv("AIVEN_TOKEN")