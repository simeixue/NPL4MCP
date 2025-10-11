# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.query
# lines: 205-206
    async def query(self, query: Dict[str, Any], params: Dict[str, Any] | None) -> CommandResponse:
        return await self.execute_command("fibery.entity/query", {"query": query, "params": params})