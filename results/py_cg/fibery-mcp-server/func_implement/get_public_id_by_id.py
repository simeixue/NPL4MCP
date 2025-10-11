# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.get_public_id_by_id
# lines: 297-309
    async def get_public_id_by_id(self, database: str, fibery_id: str) -> str | None:
        result = await self.query(
            {
                "q/from": database,
                "q/select": {"Public Id": "fibery/public-id"},
                "q/where": ["=", ["fibery/id"], "$id"],
                "q/limit": 1,
            },
            {"$id": fibery_id},
        )
        if not result.success:
            return None
        return str(result.result[0]["Public Id"])