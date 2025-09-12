# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/indexes.py
# module: src.meilisearch_mcp.indexes
# qname: src.meilisearch_mcp.indexes.IndexManager.create_index
# lines: 20-27
    def create_index(
        self, uid: str, primary_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new index"""
        try:
            return self.client.create_index(uid, {"primaryKey": primary_key})
        except Exception as e:
            raise Exception(f"Failed to create index: {str(e)}")