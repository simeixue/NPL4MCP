# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.normalize_str
# lines: 120-121
def normalize_str(s: str) -> str:
    return s.replace(" ", "_").replace("-", "_")