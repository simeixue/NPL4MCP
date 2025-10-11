# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.compose_url
# lines: 311-312
    def compose_url(self, space: str, database: str, public_id: str) -> str:
        return f"{'https' if self.__fibery_https else 'http'}://{self.__fibery_host}/{normalize_str(space)}/{normalize_str(database)}/{public_id}"