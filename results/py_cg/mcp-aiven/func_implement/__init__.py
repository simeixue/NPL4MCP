# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_env.py
# module: mcp_aiven.mcp_env
# qname: mcp_aiven.mcp_env.AivenConfig.__init__
# lines: 24-26
    def __init__(self):
        """Initialize the configuration from environment variables."""
        self._validate_required_vars()