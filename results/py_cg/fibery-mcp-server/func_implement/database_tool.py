# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/database.py
# module: src.fibery_mcp_server.tools.database
# qname: src.fibery_mcp_server.tools.database.database_tool
# lines: 11-25
def database_tool() -> mcp.types.Tool:
    return mcp.types.Tool(
        name=database_tool_name,
        description="Get list of all fields (in format of 'Title [name]: type') in the selected Fibery database and for all related databases.",
        inputSchema={
            "type": "object",
            "properties": {
                "database_name": {
                    "type": "string",
                    "description": "Database name as defined in Fibery schema",
                }
            },
            "required": ["database_name"],
        },
    )