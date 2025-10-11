# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/utils.py
# module: src.fibery_mcp_server.utils
# qname: src.fibery_mcp_server.utils.create_entity_process_fields
# lines: 82-104
async def create_entity_process_fields(
    fibery_client: FiberyClient, schema: Schema, database: Database, fields: Dict[str, Any]
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rich_text_fields = []
    safe_fields = deepcopy(fields)
    for field_name, field_value in fields.items():
        # process rich-text fields
        if database.fields_by_name().get(field_name, None).is_rich_text():
            rich_text_fields.append({"name": field_name, "value": field_value})
            safe_fields.pop(field_name)

        # process workflow fields
        if database.fields_by_name().get(field_name, None).is_workflow():
            if not isinstance(field_value, str):
                raise ValueError(f"Workflow field '{field_name}' should be a string")
        # process enum fields
        field_type = database.fields_by_name().get(field_name, None).type
        if schema.databases_by_name()[field_type].is_enum():
            enum_values_response = await fibery_client.get_enum_values(field_type)
            enum_values = enum_values_response.result
            safe_fields[field_name] = {"fibery/id": next(filter(lambda e: e["Name"] == field_value, enum_values))["Id"]}

    return rich_text_fields, safe_fields