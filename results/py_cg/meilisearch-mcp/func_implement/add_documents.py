# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.add_documents
# lines: 72-83
    def add_documents(
        self,
        index_uid: str,
        documents: List[Dict[str, Any]],
        primary_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Add documents to an index"""
        try:
            index = self.client.index(index_uid)
            return index.add_documents(documents, primary_key)
        except Exception as e:
            raise Exception(f"Failed to add documents: {str(e)}")