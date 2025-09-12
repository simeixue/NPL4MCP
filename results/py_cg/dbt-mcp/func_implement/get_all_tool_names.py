# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/tools/tool_names.py
# module: src.dbt_mcp.tools.tool_names
# qname: src.dbt_mcp.tools.tool_names.ToolName.get_all_tool_names
# lines: 55-57
    def get_all_tool_names(cls) -> set[str]:
        """Returns a set of all tool names as strings."""
        return {member.value for member in cls}