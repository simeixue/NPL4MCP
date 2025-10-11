# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/query.py
# module: src.fibery_mcp_server.tools.query
# qname: src.fibery_mcp_server.tools.query.handle_query
# lines: 90-128
async def handle_query(fibery_client: FiberyClient, arguments: Dict[str, Any]) -> List[mcp.types.TextContent]:
    q_from, q_select = arguments["q_from"], arguments["q_select"]

    schema: Schema = await fibery_client.get_schema()
    database = schema.databases_by_name()[arguments["q_from"]]
    rich_text_fields, safe_q_select = get_rich_text_fields(q_select, database)

    base = {
        "q/from": q_from,
        "q/select": safe_q_select,
        "q/limit": arguments.get("q_limit", 50),
    }
    optional = {
        k: v
        for k, v in {
            "q/where": arguments.get("q_where", None),
            "q/order-by": parse_q_order_by(arguments.get("q_order_by", None)),
            "q/offset": arguments.get("q_offset", None),
        }.items()
        if v is not None
    }
    query = base | optional

    commandResult = await fibery_client.query(query, arguments.get("q_params", None))

    if not commandResult.success:
        return [mcp.types.TextContent(type="text", text=str(commandResult))]

    for i, entity in enumerate(commandResult.result):
        for field in rich_text_fields:
            secret = entity.get(field["alias"], None)
            if not secret:
                return [
                    mcp.types.TextContent(
                        type="text", text=f"Unable to get document content for entity {entity}. Field: {field}"
                    )
                ]
            entity[field["alias"]] = await fibery_client.get_document_content(secret)
    return [mcp.types.TextContent(type="text", text=str(commandResult))]