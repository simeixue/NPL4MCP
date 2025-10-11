# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.execute_command
# lines: 190-203
    async def execute_command(self, command: str, args: Dict[str, Any]) -> CommandResponse:
        result = await self.fetch_from_fibery(
            "/api/commands",
            method="POST",
            json_data=[
                {
                    "command": command,
                    "args": args,
                },
            ],
        )

        result = result["data"][0]
        return CommandResponse(result["success"], result["result"])