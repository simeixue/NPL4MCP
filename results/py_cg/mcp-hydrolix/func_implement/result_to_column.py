# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_server.py
# module: mcp_hydrolix.mcp_server
# qname: mcp_hydrolix.mcp_server.result_to_column
# lines: 95-96
def result_to_column(query_columns, result) -> List[Column]:
    return [Column(**dict(zip(query_columns, row))) for row in result]