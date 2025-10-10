# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_server.py
# module: mcp_clickhouse.mcp_server
# qname: mcp_clickhouse.mcp_server.result_to_column
# lines: 117-118
def result_to_column(query_columns, result) -> List[Column]:
    return [Column(**dict(zip(query_columns, row))) for row in result]