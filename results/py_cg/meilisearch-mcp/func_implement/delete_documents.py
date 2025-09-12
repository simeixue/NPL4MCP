# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.delete_documents
# lines: 105-113
    def delete_documents(
        self, index_uid: str, document_ids: List[Union[str, int]]
    ) -> Dict[str, Any]:
        """Delete multiple documents by ID"""
        try:
            index = self.client.index(index_uid)
            return index.delete_documents(document_ids)
        except Exception as e:
            raise Exception(f"Failed to delete documents: {str(e)}")