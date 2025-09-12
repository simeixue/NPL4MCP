# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/server.py
# module: src.meilisearch_mcp.server
# qname: src.meilisearch_mcp.server.MeilisearchMCPServer.update_connection
# lines: 55-66
    def update_connection(
        self, url: Optional[str] = None, api_key: Optional[str] = None
    ):
        """Update connection settings and reinitialize client if needed"""
        if url:
            self.url = url
        if api_key:
            self.api_key = api_key

        self.meili_client = MeilisearchClient(self.url, self.api_key)
        self.chat_manager = ChatManager(self.meili_client.client)
        self.logger.info("Updated Meilisearch connection settings", url=self.url)