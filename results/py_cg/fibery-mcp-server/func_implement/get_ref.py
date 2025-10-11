# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/utils.py
# module: src.fibery_mcp_server.utils
# qname: src.fibery_mcp_server.utils.get_ref
# lines: 15-23
def get_ref(schema: Schema, field: Field) -> Database | None:
    if field.is_primitive():
        return None

    ref_database = schema.databases_by_name().get(field.type, None)
    if not ref_database or ref_database.is_primitive():
        return None

    return ref_database