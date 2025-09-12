# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/indexes.py
# module: src.meilisearch_mcp.indexes
# qname: src.meilisearch_mcp.indexes.IndexManager.list_indexes
# lines: 36-41
    def list_indexes(self) -> List[Dict[str, Any]]:
        """List all indexes"""
        try:
            return self.client.get_indexes()
        except Exception as e:
            raise Exception(f"Failed to list indexes: {str(e)}")