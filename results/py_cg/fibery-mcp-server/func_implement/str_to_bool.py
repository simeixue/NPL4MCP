# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/utils.py
# module: src.fibery_mcp_server.utils
# qname: src.fibery_mcp_server.utils.str_to_bool
# lines: 68-79
def str_to_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    value = value.lower()
    true_values = ["true", "yes", "y", "1", "on"]
    false_values = ["false", "no", "n", "0", "off"]
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError(f"Cannot convert '{value}' to boolean")