# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/create_entities_batch.py
# module: src.fibery_mcp_server.tools.create_entities_batch
# qname: src.fibery_mcp_server.tools.create_entities_batch.create_entities_batch_tool
# lines: 13-34
def create_entities_batch_tool() -> mcp.types.Tool:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "descriptions", "create_entities_batch"), "r") as file:
        description = file.read()

    return mcp.types.Tool(
        name=create_entities_batch_tool_name,
        description=description,
        inputSchema={
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Fibery Database where entities will be created.",
                },
                "entities": {
                    "type": "object",
                    "description": 'List of dictionaries that define what fields to set in format [{"FieldName": value}] (i.e. [{"Product Management/Name": "My new entity"}]).',
                },
            },
            "required": ["database", "entities"],
        },
    )