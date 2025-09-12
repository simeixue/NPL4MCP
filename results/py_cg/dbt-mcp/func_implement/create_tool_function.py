# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/sql/tools.py
# module: src.dbt_mcp.sql.tools
# qname: src.dbt_mcp.sql.tools.register_sql_tools.create_tool_function
# lines: 132-153
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