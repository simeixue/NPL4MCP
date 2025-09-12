# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/keys.py
# module: src.meilisearch_mcp.keys
# qname: src.meilisearch_mcp.keys.KeyManager.update_key
# lines: 33-38
    def update_key(self, key: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing API key"""
        try:
            return self.client.update_key(key, options)
        except Exception as e:
            raise Exception(f"Failed to update key: {str(e)}")