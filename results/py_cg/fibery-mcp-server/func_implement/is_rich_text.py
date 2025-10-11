# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.is_rich_text
# lines: 24-25
    def is_rich_text(self) -> bool:
        return self.__raw_field.get("fibery/type", None) == "Collaboration~Documents/Document"