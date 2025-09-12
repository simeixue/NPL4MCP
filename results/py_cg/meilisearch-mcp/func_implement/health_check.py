# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/client.py
# module: src.meilisearch_mcp.client
# qname: src.meilisearch_mcp.client.MeilisearchClient.health_check
# lines: 35-41
    def health_check(self) -> bool:
        """Check if Meilisearch is healthy"""
        try:
            response = self.client.health()
            return response.get("status") == "available"
        except Exception:
            return False