# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_fastembed_integration.py
# module: tests.test_fastembed_integration
# qname: tests.test_fastembed_integration.TestFastEmbedProviderIntegration.test_embed_query
# lines: 39-54
    async def test_embed_query(self):
        """Test that queries can be embedded."""
        provider = FastEmbedProvider("sentence-transformers/all-MiniLM-L6-v2")
        query = "This is a test query."

        embedding = await provider.embed_query(query)

        # Check that embedding has the expected shape
        assert len(embedding) > 0

        # Embed the same query again to check consistency
        embedding2 = await provider.embed_query(query)
        assert len(embedding) == len(embedding2)

        # The embeddings should be identical for the same input
        np.testing.assert_array_almost_equal(np.array(embedding), np.array(embedding2))