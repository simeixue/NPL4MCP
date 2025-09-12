# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/sql/tools.py
# module: src.dbt_mcp.sql.tools
# qname: src.dbt_mcp.sql.tools.SqlToolsManager.close
# lines: 96-97
    async def close(cls) -> None:
        await cls._stack.aclose()