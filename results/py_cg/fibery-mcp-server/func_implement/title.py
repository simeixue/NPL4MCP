# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.title
# lines: 43-44
    def title(self) -> str:
        return self.__raw_field["fibery/name"].split("/")[-1].title()