# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.__init__
# lines: 51-53
    def __init__(self):
        """Initialize the configuration from environment variables."""
        self._validate_required_vars()