# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.get_document_content
# lines: 230-236
    async def get_document_content(self, secret: str) -> str:
        result = await self.fetch_from_fibery(
            f"api/documents/{secret}?format=md",
            method="GET",
        )
        result = result["data"]
        return GetDocumentResponse(result["secret"], result["content"]).content