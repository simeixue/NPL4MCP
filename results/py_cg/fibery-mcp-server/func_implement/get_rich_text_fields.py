# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/query.py
# module: src.fibery_mcp_server.tools.query
# qname: src.fibery_mcp_server.tools.query.get_rich_text_fields
# lines: 77-87
def get_rich_text_fields(q_select: Dict[str, Any], database: Database) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rich_text_fields = []
    safe_q_select = deepcopy(q_select)
    for field_alias, field_name in safe_q_select.items():
        if not isinstance(field_name, str):
            if isinstance(field_name, list):
                field_name = field_name[0]
        if database.fields_by_name().get(field_name, None).is_rich_text():
            rich_text_fields.append({"alias": field_alias, "name": field_name})
            safe_q_select[field_alias] = [field_name, "Collaboration~Documents/secret"]
    return rich_text_fields, safe_q_select