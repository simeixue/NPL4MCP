# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/embeddings/fastembed.py
# module: src.mcp_server_qdrant.embeddings.fastembed
# qname: src.mcp_server_qdrant.embeddings.fastembed.FastEmbedProvider.get_vector_size
# lines: 45-50
    def get_vector_size(self) -> int:
        """Get the size of the vector for the Qdrant collection."""
        model_description: DenseModelDescription = (
            self.embedding_model._get_model_description(self.model_name)
        )
        return model_description.dim