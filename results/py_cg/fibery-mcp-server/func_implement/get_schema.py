# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.get_schema
# lines: 176-188
    async def get_schema(self) -> Schema:
        """
        Returns:
            Processed Fibery schema
        """
        result = await self.fetch_from_fibery(
            "/api/schema",
            method="GET",
            params={"with-description": "true", "with-soft-deleted": "false"},
        )

        schema_data = result["data"]
        return Schema(schema_data)