# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/database.py
# module: src.fibery_mcp_server.tools.database
# qname: src.fibery_mcp_server.tools.database.handle_database
# lines: 35-61
async def handle_database(fibery_client: FiberyClient, arguments: Dict[str, Any]) -> List[mcp.types.TextContent]:
    schema: Schema = await fibery_client.get_schema()

    database_name: str = arguments.get("database_name")
    if not database_name:
        return [mcp.types.TextContent(type="text", text="Error: database_name is not provided.")]

    database: Database | None = schema.databases_by_name().get(database_name, None)
    if not database:
        return [mcp.types.TextContent(type="text", text=f"Error: database {database_name} was not found.")]

    db_fields: List[Field] = database.fields

    if not db_fields:
        return [mcp.types.TextContent(type="text", text="There are no fields found in this Fibery database.")]

    prettified_fields, external_databases = await prettify_fields(
        fibery_client, schema, database, collect_external_databases=True
    )
    external_prettified_databases = [
        (db.name, (await prettify_fields(fibery_client, schema, db))[0]) for db in external_databases
    ]

    content = ""
    for db, fields in [(database.name, prettified_fields)] + external_prettified_databases:
        content += describe_database(db, fields)
    return [mcp.types.TextContent(type="text", text=content)]