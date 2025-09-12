# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/embeddings/fastembed.py
# module: src.mcp_server_qdrant.embeddings.fastembed
# qname: src.mcp_server_qdrant.embeddings.fastembed.FastEmbedProvider.embed_documents
# lines: 19-26
    async def embed_documents(self, documents: list[str]) -> list[list[float]]:
        """Embed a list of documents into vectors."""
        # Run in a thread pool since FastEmbed is synchronous
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(
            None, lambda: list(self.embedding_model.passage_embed(documents))
        )
        return [embedding.tolist() for embedding in embeddings]