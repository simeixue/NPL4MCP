# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.delete_entity
# lines: 286-295
    async def delete_entity(self, database: str, fibery_id: str) -> CommandResponse:
        return await self.execute_command(
            "fibery.entity/delete",
            {
                "type": database,
                "entity": {
                    "fibery/id": fibery_id,
                },
            },
        )