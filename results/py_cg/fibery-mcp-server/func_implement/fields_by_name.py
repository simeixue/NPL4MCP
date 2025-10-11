# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Database.fields_by_name
# lines: 67-68
    def fields_by_name(self) -> Dict[str, Field]:
        return {field.name: field for field in self.__fields}