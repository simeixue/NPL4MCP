# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_server.py
# module: mcp_clickhouse.mcp_server
# qname: mcp_clickhouse.mcp_server.chdb_initial_prompt
# lines: 329-331
def chdb_initial_prompt() -> str:
    """This prompt helps users understand how to interact and perform common operations in chDB"""
    return CHDB_PROMPT