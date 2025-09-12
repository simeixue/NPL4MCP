# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/indexes.py
# module: src.meilisearch_mcp.indexes
# qname: src.meilisearch_mcp.indexes.IndexManager.delete_index
# lines: 43-48
    def delete_index(self, uid: str) -> Dict[str, Any]:
        """Delete an index"""
        try:
            return self.client.delete_index(uid)
        except Exception as e:
            raise Exception(f"Failed to delete index: {str(e)}")