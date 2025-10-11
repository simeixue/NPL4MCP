# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.create_entity
# lines: 254-261
    async def create_entity(self, database: str, entity: Dict[str, Any]) -> CommandResponse:
        return await self.execute_command(
            "fibery.entity/create",
            {
                "type": database,
                "entity": entity,
            },
        )