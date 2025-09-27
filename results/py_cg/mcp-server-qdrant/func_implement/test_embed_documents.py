# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_fastembed_integration.py
# module: tests.test_fastembed_integration
# qname: tests.test_fastembed_integration.TestFastEmbedProviderIntegration.test_embed_documents
# lines: 18-37
    async def test_embed_documents(self):
        """Test that documents can be embedded."""
        provider = FastEmbedProvider("sentence-transformers/all-MiniLM-L6-v2")
        documents = ["This is a test document.", "This is another test document."]

        embeddings = await provider.embed_documents(documents)

        # Check that we got the right number of embeddings
        assert len(embeddings) == len(documents)

        # Check that embeddings have the expected shape
        # The exact dimension depends on the model, but should be consistent
        assert len(embeddings[0]) > 0
        assert all(len(embedding) == len(embeddings[0]) for embedding in embeddings)

        # Check that embeddings are different for different documents
        # Convert to numpy arrays for easier comparison
        embedding1 = np.array(embeddings[0])
        embedding2 = np.array(embeddings[1])
        assert not np.array_equal(embedding1, embedding2)