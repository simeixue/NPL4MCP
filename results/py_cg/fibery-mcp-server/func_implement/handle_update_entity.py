# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/update_entity.py
# module: src.fibery_mcp_server.tools.update_entity
# qname: src.fibery_mcp_server.tools.update_entity.handle_update_entity
# lines: 65-120
async def handle_update_entity(fibery_client: FiberyClient, arguments: Dict[str, Any]) -> List[mcp.types.TextContent]:
    database_name: str = arguments.get("database")
    entity: Dict[str, Any] = arguments.get("entity")

    if not database_name:
        return [mcp.types.TextContent(type="text", text="Error: database is not provided.")]

    if not entity:
        return [mcp.types.TextContent(type="text", text="Error: entity is not provided.")]

    if not entity["fibery/id"]:
        return [
            mcp.types.TextContent(
                type="text", text="Error: entity id is not provided. Use 'fibery/id' field to set it."
            )
        ]

    schema = await fibery_client.get_schema()
    database = schema.databases_by_name()[database_name]
    if not database:
        return [mcp.types.TextContent(type="text", text=f"Error: database {database_name} was not found.")]
    rich_text_fields, safe_entity = await process_fields(fibery_client, schema, database, entity)

    update_result = await fibery_client.update_entity(database_name, safe_entity)

    if not update_result.success:
        return [mcp.types.TextContent(type="text", text=str(update_result))]

    if len(rich_text_fields) > 0:
        secrets_response = await fibery_client.query(
            {
                "q/from": database_name,
                "q/select": {
                    field["name"]: [field["name"], "Collaboration~Documents/secret"] for field in rich_text_fields
                },
                "q/limit": 1,
                "q/where": ["=", ["fibery/id"], "$id"],
            },
            {"$id": safe_entity["fibery/id"]},
        )

        for field, secret_response in zip(rich_text_fields, secrets_response.result):
            secret = secret_response.get(field["name"], None)
            if not secret:
                return [
                    mcp.types.TextContent(
                        type="text", text=f"Error: entity created, but could you populate document {field['name']}"
                    )
                ]
            doc_result = await fibery_client.create_or_update_document(secret, field["value"], append=field["append"])
            if not doc_result.success:
                return [mcp.types.TextContent(type="text", text=str(doc_result))]

    public_id = await fibery_client.get_public_id_by_id(database_name, safe_entity["fibery/id"])
    url = fibery_client.compose_url(database_name.split("/")[0], database_name.split("/")[1], public_id)
    return [mcp.types.TextContent(type="text", text=str(f"Entity updated successfully. URL: {url}"))]