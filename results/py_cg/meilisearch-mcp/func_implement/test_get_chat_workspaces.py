# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_get_chat_workspaces
# lines: 106-115
    async def test_get_chat_workspaces(self, setup_mock_chat_client):
        """Test getting chat workspaces"""
        server = setup_mock_chat_client

        result = await server.chat_manager.get_chat_workspaces(offset=0, limit=10)

        assert "results" in result
        assert len(result["results"]) == 2
        assert result["results"][0]["uid"] == "workspace1"
        assert result["total"] == 2