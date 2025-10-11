# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.create_or_update_document
# lines: 238-252
    async def create_or_update_document(
        self, secret: str, content: str, append: bool = False
    ) -> CreateDocumentResponse:
        result = await self.fetch_from_fibery(
            "/api/documents/commands",
            "POST",
            {
                "command": "create-or-update-documents" if not append else "create-or-append-documents",
                "args": [{"secret": secret, "content": content}],
            },
        )
        result_parsed: bool | Dict[str, Any] = result["data"]
        if result_parsed is True:
            return CreateDocumentResponse(True, "Document created/updated successfully")
        return CreateDocumentResponse(False, result_parsed.get("message", "Failed to create/update document."))