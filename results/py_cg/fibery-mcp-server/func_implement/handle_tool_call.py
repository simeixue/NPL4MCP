# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/__init__.py
# module: src.fibery_mcp_server.tools.__init__
# qname: src.fibery_mcp_server.tools.__init__.handle_tool_call
# lines: 19-35
async def handle_tool_call(fibery_client: FiberyClient, name: str, arguments: Dict[str, Any]):
    if name == schema_tool_name:
        return await handle_schema(fibery_client)
    elif name == database_tool_name:
        return await handle_database(fibery_client, arguments)
    elif name == query_tool_name:
        return await handle_query(fibery_client, arguments)
    elif name == current_date_tool_name:
        return await handle_current_date()
    elif name == create_entity_tool_name:
        return await handle_create_entity(fibery_client, arguments)
    elif name == create_entities_batch_tool_name:
        return await handle_create_entities_batch(fibery_client, arguments)
    elif name == update_entity_tool_name:
        return await handle_update_entity(fibery_client, arguments)
    else:
        return [mcp.types.TextContent(type="text", text=f"Error: Unknown tool {name}")]