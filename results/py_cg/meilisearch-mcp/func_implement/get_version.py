# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/client.py
# module: src.meilisearch_mcp.client
# qname: src.meilisearch_mcp.client.MeilisearchClient.get_version
# lines: 43-45
    def get_version(self) -> Dict[str, Any]:
        """Get Meilisearch version information"""
        return self.client.get_version()