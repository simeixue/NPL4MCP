# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_settings.py
# module: tests.test_settings
# qname: tests.test_settings.TestQdrantSettings.test_default_values
# lines: 14-18
    def test_default_values(self):
        """Test that required fields raise errors when not provided."""

        # Should not raise error because there are no required fields
        QdrantSettings()