# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/indexes.py
# module: src.meilisearch_mcp.indexes
# qname: src.meilisearch_mcp.indexes.IndexManager.update_index
# lines: 50-55
    def update_index(self, uid: str, primary_key: str) -> Dict[str, Any]:
        """Update index primary key"""
        try:
            return self.client.update_index(uid, {"primaryKey": primary_key})
        except Exception as e:
            raise Exception(f"Failed to update index: {str(e)}")