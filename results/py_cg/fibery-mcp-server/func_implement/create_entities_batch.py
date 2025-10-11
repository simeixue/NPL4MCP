# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.create_entities_batch
# lines: 263-275
    async def create_entities_batch(self, database: str, entities: List[Dict[str, Any]]) -> CommandResponse:
        return await self.execute_command(
            "fibery.command/batch",
            {
                "commands": list(map(lambda entity: {
                    "command": "fibery.entity/create",
                    "args": {
                        "type": database,
                        "entity": entity
                    }
                }, entities)),
            },
        )