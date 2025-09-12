# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.update_documents
# lines: 85-93
    def update_documents(
        self, index_uid: str, documents: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Update documents in an index"""
        try:
            index = self.client.index(index_uid)
            return index.update_documents(documents)
        except Exception as e:
            raise Exception(f"Failed to update documents: {str(e)}")