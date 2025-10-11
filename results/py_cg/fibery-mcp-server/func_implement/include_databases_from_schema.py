# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Schema.include_databases_from_schema
# lines: 87-95
    def include_databases_from_schema(self) -> List[Database]:
        if not self.__databases:
            return []

        databases: List[Database] = []

        for database in filter(lambda db: db.include_database(), self.__databases):
            databases.append(database)
        return databases