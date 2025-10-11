# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.is_title
# lines: 18-19
    def is_title(self) -> bool:
        return self.__raw_meta.get("ui/title?", False)