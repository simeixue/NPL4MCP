# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/mcp/server.py
# module: src.dbt_mcp.mcp.server
# qname: src.dbt_mcp.mcp.server.DbtMCP.__init__
# lines: 48-57
    def __init__(
        self,
        config: Config,
        usage_tracker: UsageTracker,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.usage_tracker = usage_tracker
        self.config = config