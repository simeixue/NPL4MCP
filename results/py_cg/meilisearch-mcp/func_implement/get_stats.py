# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/client.py
# module: src.meilisearch_mcp.client
# qname: src.meilisearch_mcp.client.MeilisearchClient.get_stats
# lines: 47-49
    def get_stats(self) -> Dict[str, Any]:
        """Get database stats"""
        return self.client.get_all_stats()