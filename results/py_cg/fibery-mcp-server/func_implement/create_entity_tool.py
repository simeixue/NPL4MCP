# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/create_entity.py
# module: src.fibery_mcp_server.tools.create_entity
# qname: src.fibery_mcp_server.tools.create_entity.create_entity_tool
# lines: 13-34
def create_entity_tool() -> mcp.types.Tool:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "descriptions", "create_entity"), "r") as file:
        description = file.read()

    return mcp.types.Tool(
        name=create_entity_tool_name,
        description=description,
        inputSchema={
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Fibery Database where to create an entity.",
                },
                "entity": {
                    "type": "object",
                    "description": 'Dictionary that defines what fields to set in format {"FieldName": value} (i.e. {"Product Management/Name": "My new entity"}).',
                },
            },
            "required": ["database", "entity"],
        },
    )