# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.delete_all_documents
# lines: 115-121
    def delete_all_documents(self, index_uid: str) -> Dict[str, Any]:
        """Delete all documents in an index"""
        try:
            index = self.client.index(index_uid)
            return index.delete_all_documents()
        except Exception as e:
            raise Exception(f"Failed to delete all documents: {str(e)}")