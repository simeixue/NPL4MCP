# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.get_document
# lines: 62-70
    def get_document(
        self, index_uid: str, document_id: Union[str, int]
    ) -> Dict[str, Any]:
        """Get a single document"""
        try:
            index = self.client.index(index_uid)
            return index.get_document(document_id)
        except Exception as e:
            raise Exception(f"Failed to get document: {str(e)}")