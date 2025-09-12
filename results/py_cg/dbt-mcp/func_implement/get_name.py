# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/tools/definitions.py
# module: src.dbt_mcp.tools.definitions
# qname: src.dbt_mcp.tools.definitions.ToolDefinition.get_name
# lines: 18-19
    def get_name(self) -> str:
        return self.name or self.fn.__name__