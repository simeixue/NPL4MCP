# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_server.py
# module: mcp_clickhouse.mcp_server
# qname: mcp_clickhouse.mcp_server.execute_query
# lines: 179-188
def execute_query(query: str):
    client = create_clickhouse_client()
    try:
        read_only = get_readonly_setting(client)
        res = client.query(query, settings={"readonly": read_only})
        logger.info(f"Query returned {len(res.result_rows)} rows")
        return {"columns": res.column_names, "rows": res.result_rows}
    except Exception as err:
        logger.error(f"Error executing query: {err}")
        raise ToolError(f"Query execution failed: {str(err)}")