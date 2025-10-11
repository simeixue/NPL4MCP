# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.get_enum_values
# lines: 208-228
    async def get_enum_values(self, database_name: str) -> CommandResponse:
        result = await self.fetch_from_fibery(
            "/api/commands",
            method="POST",
            json_data=[
                {
                    "command": "fibery.entity/query",
                    "args": {
                        "query": {
                            "q/from": database_name,
                            "q/select": {"Id": ["fibery/id"], "Name": ["enum/name"]},
                            "q/limit": 100,
                        },
                        "params": {},
                    },
                },
            ],
        )

        result = result["data"][0]
        return CommandResponse(result["success"], result["result"])