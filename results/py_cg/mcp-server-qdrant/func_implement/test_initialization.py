# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_fastembed_integration.py
# module: tests.test_fastembed_integration
# qname: tests.test_fastembed_integration.TestFastEmbedProviderIntegration.test_initialization
# lines: 12-16
    async def test_initialization(self):
        """Test that the provider can be initialized with a valid model."""
        provider = FastEmbedProvider("sentence-transformers/all-MiniLM-L6-v2")
        assert provider.model_name == "sentence-transformers/all-MiniLM-L6-v2"
        assert isinstance(provider.embedding_model, TextEmbedding)