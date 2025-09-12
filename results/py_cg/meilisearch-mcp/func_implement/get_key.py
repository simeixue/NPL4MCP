# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/keys.py
# module: src.meilisearch_mcp.keys
# qname: src.meilisearch_mcp.keys.KeyManager.get_key
# lines: 19-24
    def get_key(self, key: str) -> Dict[str, Any]:
        """Get information about a specific key"""
        try:
            return self.client.get_key(key)
        except Exception as e:
            raise Exception(f"Failed to get key: {str(e)}")