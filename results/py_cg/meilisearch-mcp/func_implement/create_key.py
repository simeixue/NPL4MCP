# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/keys.py
# module: src.meilisearch_mcp.keys
# qname: src.meilisearch_mcp.keys.KeyManager.create_key
# lines: 26-31
    def create_key(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new API key"""
        try:
            return self.client.create_key(options)
        except Exception as e:
            raise Exception(f"Failed to create key: {str(e)}")