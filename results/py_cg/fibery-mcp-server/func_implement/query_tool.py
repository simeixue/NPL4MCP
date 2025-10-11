# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/query.py
# module: src.fibery_mcp_server.tools.query
# qname: src.fibery_mcp_server.tools.query.query_tool
# lines: 12-68
def query_tool() -> mcp.types.Tool:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "descriptions", "query"), "r") as file:
        description = file.read()

    return mcp.types.Tool(
        name=query_tool_name,
        description=description,
        inputSchema={
            "type": "object",
            "properties": {
                "q_from": {
                    "type": "string",
                    "description": 'Specifies the entity type in "Space/Type" format (e.g., "Product Management/feature", "Product Management/Insight")',
                },
                "q_select": {
                    "type": "object",
                    "description": "\n".join(
                        [
                            "Defines what fields to retrieve. Can include:",
                            '  - Primitive fields using format {"AliasName": "FieldName"} (i.e. {"Name": "Product Management/Name"})',
                            '  - Related entity fields using format {"AliasName": ["Related entity", "related entity field"]} (i.e. {"Secret": ["Product Management/Description", "Collaboration~Documents/secret"]}). Careful, does not work with 1-* connection!',
                            'To work with 1-* relationships, you can use sub-querying: {"AliasName": {"q/from": "Related type", "q/select": {"AliasName 2": "fibery/id"}, "q/limit": 50}}',
                            "AliasName can be of any arbitrary value.",
                        ]
                    ),
                },
                "q_where": {
                    "type": "object",
                    "description": "\n".join(
                        [
                            'Filter conditions in format [operator, [field_path], value] or ["q/and"|"q/or", ...conditions]. Common usages:',
                            '- Simple comparison: ["=", ["field", "path"], "$param"]. You cannot pass value of $param directly in where clause. Use params object instead. Pay really close attention to it as it is not common practice, but that\'s how it works in our case!',
                            '- Logical combinations: ["q/and", ["<", ["field1"], "$param1"], ["=", ["field2"], "$param2"]]',
                            "- Available operators: =, !=, <, <=, >, >=, q/contains, q/not-contains, q/in, q/not-in",
                        ]
                    ),
                },
                "q_order_by": {
                    "type": "object",
                    "description": 'List of sorting criteria in format {"field1": "q/asc", "field2": "q/desc"}',
                },
                "q_limit": {
                    "type": "integer",
                    "description": "Number of results per page (defaults to 50). Maximum allowed value is 1000",
                },
                "q_offset": {
                    "type": "integer",
                    "description": "Number of results to skip. Mainly used in combination with limit and orderBy for pagination.",
                },
                "q_params": {
                    "type": "object",
                    "description": 'Dictionary of parameter values referenced in where using "$param" syntax. For example, {$fromDate: "2025-01-01"}',
                },
            },
            "required": ["q_from", "q_select"],
        },
    )