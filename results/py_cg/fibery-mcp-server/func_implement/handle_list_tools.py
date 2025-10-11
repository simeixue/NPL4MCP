# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/__init__.py
# module: src.fibery_mcp_server.tools.__init__
# qname: src.fibery_mcp_server.tools.__init__.handle_list_tools
# lines: 15-16
def handle_list_tools():
    return [current_date_tool(), schema_tool(), database_tool(), query_tool(), create_entity_tool(), create_entities_batch_tool(), update_entity_tool()]