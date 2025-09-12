# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/embeddings/fastembed.py
# module: src.mcp_server_qdrant.embeddings.fastembed
# qname: src.mcp_server_qdrant.embeddings.fastembed.FastEmbedProvider.get_vector_name
# lines: 37-43
    def get_vector_name(self) -> str:
        """
        Return the name of the vector for the Qdrant collection.
        Important: This is compatible with the FastEmbed logic used before 0.6.0.
        """
        model_name = self.embedding_model.model_name.split("/")[-1].lower()
        return f"fast-{model_name}"