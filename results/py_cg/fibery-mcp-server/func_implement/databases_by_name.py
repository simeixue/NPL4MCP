# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Schema.databases_by_name
# lines: 84-85
    def databases_by_name(self) -> Dict[str, Database]:
        return {db.name: db for db in self.__databases}