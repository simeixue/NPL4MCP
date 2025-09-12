# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_fastembed_integration.py
# module: tests.test_fastembed_integration
# qname: tests.test_fastembed_integration.TestFastEmbedProviderIntegration.test_get_vector_name
# lines: 56-63
    async def test_get_vector_name(self):
        """Test that the vector name is generated correctly."""
        provider = FastEmbedProvider("sentence-transformers/all-MiniLM-L6-v2")
        vector_name = provider.get_vector_name()

        # Check that the vector name follows the expected format
        assert vector_name.startswith("fast-")
        assert "minilm" in vector_name.lower()