# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_server.py
# module: mcp_hydrolix.mcp_server
# qname: mcp_hydrolix.mcp_server.result_to_table
# lines: 91-92
def result_to_table(query_columns, result) -> List[Table]:
    return [Table(**dict(zip(query_columns, row))) for row in result]