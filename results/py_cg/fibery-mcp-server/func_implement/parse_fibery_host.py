# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/utils.py
# module: src.fibery_mcp_server.utils
# qname: src.fibery_mcp_server.utils.parse_fibery_host
# lines: 107-108
def parse_fibery_host(fibery_host: str) -> str:
    return fibery_host.replace("https://", "")