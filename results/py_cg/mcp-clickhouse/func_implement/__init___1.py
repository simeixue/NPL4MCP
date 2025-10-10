# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ChDBConfig.__init__
# lines: 218-221
    def __init__(self):
        """Initialize the configuration from environment variables."""
        if self.enabled:
            self._validate_required_vars()