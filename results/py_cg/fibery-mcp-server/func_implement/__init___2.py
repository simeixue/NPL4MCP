# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Schema.__init__
# lines: 80-82
    def __init__(self, raw_schema: Dict[str, Any]):
        self.__raw_schema: Dict[str, Any] = raw_schema
        self.__databases: List[Database] = [Database(raw_db) for raw_db in raw_schema["fibery/types"]]