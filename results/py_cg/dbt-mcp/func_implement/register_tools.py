# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/tools/register.py
# module: src.dbt_mcp.tools.register
# qname: src.dbt_mcp.tools.register.register_tools
# lines: 9-25
def register_tools(
    dbt_mcp: FastMCP,
    tool_definitions: list[ToolDefinition],
    exclude_tools: Sequence[ToolName] = [],
) -> None:
    for tool_definition in tool_definitions:
        if tool_definition.get_name().lower() in [
            tool.value.lower() for tool in exclude_tools
        ]:
            continue
        dbt_mcp.tool(
            name=tool_definition.get_name(),
            title=tool_definition.title,
            description=tool_definition.description,
            annotations=tool_definition.annotations,
            structured_output=tool_definition.structured_output,
        )(tool_definition.fn)