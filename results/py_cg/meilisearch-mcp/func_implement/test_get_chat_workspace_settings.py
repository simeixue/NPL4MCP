# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_get_chat_workspace_settings
# lines: 118-128
    async def test_get_chat_workspace_settings(self, setup_mock_chat_client):
        """Test getting chat workspace settings"""
        server = setup_mock_chat_client

        result = await server.chat_manager.get_chat_workspace_settings(
            workspace_uid="workspace1"
        )

        assert result["model"] == "gpt-3.5-turbo"
        assert "indexUids" in result
        assert result["temperature"] == 0.7