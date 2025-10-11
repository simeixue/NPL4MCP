# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Database.__init__
# lines: 48-51
    def __init__(self, raw_database: Dict[str, Any]):
        self.__raw_database = raw_database
        self.__raw_meta = raw_database.get("fibery/meta", {})
        self.__fields: List[Field] = [Field(raw_field) for raw_field in raw_database["fibery/fields"]]