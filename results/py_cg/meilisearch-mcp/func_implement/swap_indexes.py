# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/indexes.py
# module: src.meilisearch_mcp.indexes
# qname: src.meilisearch_mcp.indexes.IndexManager.swap_indexes
# lines: 57-62
    def swap_indexes(self, indexes: List[List[str]]) -> Dict[str, Any]:
        """Swap indexes"""
        try:
            return self.client.swap_indexes(indexes)
        except Exception as e:
            raise Exception(f"Failed to swap indexes: {str(e)}")