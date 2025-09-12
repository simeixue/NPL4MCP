# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_env.py
# module: mcp_aiven.mcp_env
# qname: mcp_aiven.mcp_env.AivenConfig.url
# lines: 29-31
    def url(self) -> str:
        """Get the Aiven Base URL."""
        return os.getenv("AIVEN_BASE_URL")