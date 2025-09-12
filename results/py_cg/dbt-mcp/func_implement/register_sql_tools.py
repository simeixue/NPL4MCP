# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/sql/tools.py
# module: src.dbt_mcp.sql.tools
# qname: src.dbt_mcp.sql.tools.register_sql_tools
# lines: 100-165
async def register_sql_tools(
    dbt_mcp: FastMCP,
    config: SqlConfig,
    exclude_tools: Sequence[ToolName] = [],
) -> None:
    """
    Register SQL MCP tools.

    SQL tools are hosted remotely, so their definitions aren't found in this repo.
    """

    is_local = config.host and config.host.startswith("localhost")
    path = "/v1/mcp/" if is_local else "/api/ai/v1/mcp/"
    scheme = "http://" if is_local else "https://"
    host_prefix = f"{config.host_prefix}." if config.host_prefix else ""
    url = f"{scheme}{host_prefix}{config.host}{path}"
    headers = {
        "Authorization": f"Bearer {config.token}",
        "x-dbt-prod-environment-id": str(config.prod_environment_id),
        "x-dbt-dev-environment-id": str(config.dev_environment_id),
        "x-dbt-user-id": str(config.user_id),
    }
    sql_tools_manager = SqlToolsManager()
    session = await sql_tools_manager.get_remote_mcp_session(url, headers)
    await session.initialize()
    sql_tools = await _get_sql_tools(session)
    logger.info(f"Loaded sql tools: {', '.join([tool.name for tool in sql_tools])}")
    for tool in sql_tools:
        if tool.name.lower() in [tool.value.lower() for tool in exclude_tools]:
            continue

        # Create a new function using a factory to avoid closure issues
        def create_tool_function(tool_name: str):
            async def tool_function(*args, **kwargs) -> Sequence[ContentBlock]:
                try:
                    tool_call_result = await session.call_tool(
                        tool_name,
                        kwargs,
                    )
                    if tool_call_result.isError:
                        raise ValueError(
                            f"Tool {tool_name} reported an error: "
                            + f"{tool_call_result.content}"
                        )
                    return tool_call_result.content
                except Exception as e:
                    return [
                        TextContent(
                            type="text",
                            text=str(e),
                        )
                    ]

            return tool_function

        dbt_mcp._tool_manager._tools[tool.name] = InternalTool(
            fn=create_tool_function(tool.name),
            title=tool.title,
            name=tool.name,
            annotations=tool.annotations,
            description=tool.description or "",
            parameters=tool.inputSchema,
            fn_metadata=get_remote_tool_fn_metadata(tool),
            is_async=True,
            context_kwarg=None,
        )