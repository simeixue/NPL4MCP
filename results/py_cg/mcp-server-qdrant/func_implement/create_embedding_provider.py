# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/embeddings/factory.py
# module: src.mcp_server_qdrant.embeddings.factory
# qname: src.mcp_server_qdrant.embeddings.factory.create_embedding_provider
# lines: 6-17
def create_embedding_provider(settings: EmbeddingProviderSettings) -> EmbeddingProvider:
    """
    Create an embedding provider based on the specified type.
    :param settings: The settings for the embedding provider.
    :return: An instance of the specified embedding provider.
    """
    if settings.provider_type == EmbeddingProviderType.FASTEMBED:
        from mcp_server_qdrant.embeddings.fastembed import FastEmbedProvider

        return FastEmbedProvider(settings.model_name)
    else:
        raise ValueError(f"Unsupported embedding provider: {settings.provider_type}")