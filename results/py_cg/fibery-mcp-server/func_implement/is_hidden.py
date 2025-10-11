# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.is_hidden
# lines: 21-22
    def is_hidden(self) -> bool:
        return self.__raw_meta.get("ui/hidden?", False)