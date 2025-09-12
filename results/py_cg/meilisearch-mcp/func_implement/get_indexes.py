# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/client.py
# module: src.meilisearch_mcp.client
# qname: src.meilisearch_mcp.client.MeilisearchClient.get_indexes
# lines: 104-124
    def get_indexes(self) -> Dict[str, Any]:
        """Get all indexes"""
        indexes = self.client.get_indexes()
        # Convert Index objects to serializable dictionaries
        serialized_indexes = []
        for index in indexes["results"]:
            serialized_indexes.append(
                {
                    "uid": index.uid,
                    "primaryKey": index.primary_key,
                    "createdAt": index.created_at,
                    "updatedAt": index.updated_at,
                }
            )

        return {
            "results": serialized_indexes,
            "offset": indexes["offset"],
            "limit": indexes["limit"],
            "total": indexes["total"],
        }