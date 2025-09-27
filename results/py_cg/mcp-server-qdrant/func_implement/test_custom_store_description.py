# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_settings.py
# module: tests.test_settings
# qname: tests.test_settings.TestToolSettings.test_custom_store_description
# lines: 89-94
    def test_custom_store_description(self, monkeypatch):
        """Test loading custom store description from environment variable."""
        monkeypatch.setenv("TOOL_STORE_DESCRIPTION", "Custom store description")
        settings = ToolSettings()
        assert settings.tool_store_description == "Custom store description"
        assert settings.tool_find_description == DEFAULT_TOOL_FIND_DESCRIPTION