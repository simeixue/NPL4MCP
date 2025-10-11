# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.primitive_type
# lines: 35-36
    def primitive_type(self) -> str:
        return self.__raw_field["fibery/type"].split("/")[-1]