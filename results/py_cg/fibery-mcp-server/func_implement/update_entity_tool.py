# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/update_entity.py
# module: src.fibery_mcp_server.tools.update_entity
# qname: src.fibery_mcp_server.tools.update_entity.update_entity_tool
# lines: 13-39
def update_entity_tool() -> mcp.types.Tool:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "descriptions", "update_entity"), "r") as file:
        description = file.read()

    return mcp.types.Tool(
        name=update_entity_tool_name,
        description=description,
        inputSchema={
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "Fibery Database where to update an entity.",
                },
                "entity": {
                    "type": "object",
                    "description": "\n".join(
                        [
                            'Dictionary that defines what fields to set in format {"FieldName": value} (i.e. {"Product Management/Name": "My new entity"}).',
                            'Exception are document fields. For them you must specify append (boolean, whether to append to current content) and content itself: {"Product Management/Description": {"append": true, "content": "Additional info"}}',
                        ]
                    ),
                },
            },
            "required": ["database", "entity"],
        },
    )