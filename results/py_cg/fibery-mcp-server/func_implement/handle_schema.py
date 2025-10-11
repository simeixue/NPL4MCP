# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/schema.py
# module: src.fibery_mcp_server.tools.schema
# qname: src.fibery_mcp_server.tools.schema.handle_schema
# lines: 18-29
async def handle_schema(fibery_client: FiberyClient) -> List[mcp.types.TextContent]:
    schema: Schema = await fibery_client.get_schema()
    db_list: List[Database] = schema.include_databases_from_schema()

    if not db_list:
        content = "No databases found in this Fibery workspace."
    else:
        content = "Databases in Fibery workspace:\n\n"
        for i, db in enumerate(db_list, 1):
            content += f"{i}. {db.name}\n"

    return [mcp.types.TextContent(type="text", text=content)]