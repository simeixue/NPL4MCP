# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/indexes.py
# module: src.meilisearch_mcp.indexes
# qname: src.meilisearch_mcp.indexes.IndexManager.get_index
# lines: 29-34
    def get_index(self, uid: str) -> Dict[str, Any]:
        """Get index information"""
        try:
            return self.client.get_index(uid)
        except Exception as e:
            raise Exception(f"Failed to get index: {str(e)}")