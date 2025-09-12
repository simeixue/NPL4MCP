# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/keys.py
# module: src.meilisearch_mcp.keys
# qname: src.meilisearch_mcp.keys.KeyManager.get_keys
# lines: 12-17
    def get_keys(self, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get list of API keys"""
        try:
            return self.client.get_keys(parameters)
        except Exception as e:
            raise Exception(f"Failed to get keys: {str(e)}")