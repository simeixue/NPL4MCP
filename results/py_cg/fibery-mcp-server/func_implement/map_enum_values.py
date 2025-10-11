# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/utils.py
# module: src.fibery_mcp_server.utils
# qname: src.fibery_mcp_server.utils.map_enum_values
# lines: 26-27
def map_enum_values(enum_values: List[Dict[str, Any]]) -> str:
    return ", ".join([f'"{value["Name"]}"' for value in enum_values])