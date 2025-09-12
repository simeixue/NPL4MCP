# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/client/tools.py
# module: src.client.tools
# qname: src.client.tools.get_tools
# lines: 8-19
async def get_tools(dbt_mcp: DbtMCP) -> list[FunctionToolParam]:
    mcp_tools = await dbt_mcp.list_tools()
    return [
        FunctionToolParam(
            type="function",
            name=t.name,
            description=t.description,
            parameters=t.inputSchema,
            strict=False,
        )
        for t in mcp_tools
    ]