# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/sql/tools.py
# module: src.dbt_mcp.sql.tools
# qname: src.dbt_mcp.sql.tools._get_sql_tools
# lines: 63-71
async def _get_sql_tools(session: ClientSession) -> list[Tool]:
    try:
        sql_tool_names = {t.value for t in toolsets[Toolset.SQL]}
        return [
            t for t in (await session.list_tools()).tools if t.name in sql_tool_names
        ]
    except Exception as e:
        logger.error(f"Error getting SQL tools: {e}")
        return []