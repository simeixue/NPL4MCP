# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.is_primitive
# lines: 12-13
    def is_primitive(self) -> bool:
        return self.__raw_meta.get("fibery/primitive?", False)