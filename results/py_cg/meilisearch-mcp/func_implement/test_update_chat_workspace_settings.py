# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_update_chat_workspace_settings
# lines: 131-141
    async def test_update_chat_workspace_settings(self, setup_mock_chat_client):
        """Test updating chat workspace settings"""
        server = setup_mock_chat_client

        result = await server.chat_manager.update_chat_workspace_settings(
            workspace_uid="workspace1",
            settings={"model": "gpt-4", "temperature": 0.5},
        )

        assert result["model"] == "gpt-4"
        assert result["temperature"] == 0.5