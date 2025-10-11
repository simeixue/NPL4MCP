# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Database.is_enum
# lines: 56-57
    def is_enum(self) -> bool:
        return self.__raw_meta.get("fibery/enum?", False)