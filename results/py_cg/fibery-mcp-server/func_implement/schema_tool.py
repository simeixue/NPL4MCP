# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/schema.py
# module: src.fibery_mcp_server.tools.schema
# qname: src.fibery_mcp_server.tools.schema.schema_tool
# lines: 10-15
def schema_tool() -> mcp.types.Tool:
    return mcp.types.Tool(
        name=schema_tool_name,
        description="Get list of all databases (their names) in user's Fibery workspace (schema)",
        inputSchema={"type": "object"},
    )