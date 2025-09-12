# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/embeddings/fastembed.py
# module: src.mcp_server_qdrant.embeddings.fastembed
# qname: src.mcp_server_qdrant.embeddings.fastembed.FastEmbedProvider.embed_query
# lines: 28-35
    async def embed_query(self, query: str) -> list[float]:
        """Embed a query into a vector."""
        # Run in a thread pool since FastEmbed is synchronous
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(
            None, lambda: list(self.embedding_model.query_embed([query]))
        )
        return embeddings[0].tolist()