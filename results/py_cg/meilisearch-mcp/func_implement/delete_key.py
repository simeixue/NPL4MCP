# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/keys.py
# module: src.meilisearch_mcp.keys
# qname: src.meilisearch_mcp.keys.KeyManager.delete_key
# lines: 40-45
    def delete_key(self, key: str) -> None:
        """Delete an API key"""
        try:
            return self.client.delete_key(key)
        except Exception as e:
            raise Exception(f"Failed to delete key: {str(e)}")