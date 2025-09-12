# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.delete_document
# lines: 95-103
    def delete_document(
        self, index_uid: str, document_id: Union[str, int]
    ) -> Dict[str, Any]:
        """Delete a single document"""
        try:
            index = self.client.index(index_uid)
            return index.delete_document(document_id)
        except Exception as e:
            raise Exception(f"Failed to delete document: {str(e)}")