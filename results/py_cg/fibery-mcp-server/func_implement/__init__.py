# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.__init__
# lines: 8-10
    def __init__(self, raw_field: Dict[str, Any]):
        self.__raw_field = raw_field
        self.__raw_meta = raw_field.get("fibery/meta", {})