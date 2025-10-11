# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_server.py
# module: mcp_hydrolix.mcp_server
# qname: mcp_hydrolix.mcp_server.execute_query
# lines: 159-177
def execute_query(query: str):
    client = create_hydrolix_client()
    try:
        res = client.query(
            query,
            settings={
                "readonly": 1,
                "hdx_query_max_execution_time": SELECT_QUERY_TIMEOUT_SECS,
                "hdx_query_max_attempts": 1,
                "hdx_query_max_result_rows": 100_000,
                "hdx_query_max_memory_usage": 2 * 1024 * 1024 * 1024,  # 2GiB
                "hdx_query_admin_comment": f"User: {MCP_SERVER_NAME}",
            },
        )
        logger.info(f"Query returned {len(res.result_rows)} rows")
        return {"columns": res.column_names, "rows": res.result_rows}
    except Exception as err:
        logger.error(f"Error executing query: {err}")
        raise ToolError(f"Query execution failed: {str(err)}")