# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/utils.py
# module: src.fibery_mcp_server.utils
# qname: src.fibery_mcp_server.utils.prettify_fields
# lines: 30-65
async def prettify_fields(
    fibery_client: FiberyClient, schema: Schema, database: Database, collect_external_databases: bool = False
) -> Tuple[List[PrettyField], List[Database]]:
    fields = database.fields

    pretty_fields = []
    external_databases: List[Database] = []

    for field in fields:
        if field.is_hidden():
            continue
        title = field.title
        name = field.name
        field_type = field.type

        ref_database = get_ref(schema, field)
        type_str = field.primitive_type if field.is_primitive() else field_type
        if field_type == "fibery/rank":
            type_str = "int"
        if field.is_rich_text():
            type_str = "fibery/document"
        if database.is_enum() and field.is_title():
            enum_values_response = await fibery_client.get_enum_values(database.name)
            type_str += f" # available values: {map_enum_values(enum_values_response.result)}"
        if database.name.split("/")[0] == "workflow" and field.title == "Type":
            type_str += ' # available values: "Not started", "Started", "Finished"'
        if ref_database and not field.is_rich_text():
            type_str = field_type if not field.is_collection() else f"Collection({field_type})"
            if (
                collect_external_databases
                and ref_database.name != database.name
                and ref_database.name not in map(lambda db: db.name, external_databases)
            ):
                external_databases.append(ref_database)
        pretty_fields.append(PrettyField(title, name, type_str))
    return pretty_fields, external_databases