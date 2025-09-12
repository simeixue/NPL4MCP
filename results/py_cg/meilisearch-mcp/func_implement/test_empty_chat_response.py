# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_empty_chat_response
# lines: 163-179
    async def test_empty_chat_response(self, server):
        """Test handling empty chat response"""
        # Mock empty response
        server.chat_manager.client = MagicMock()

        def mock_empty_completion(*args, **kwargs):
            # Return empty chunks
            return iter([])

        server.chat_manager.client.create_chat_completion = mock_empty_completion

        result = await server.chat_manager.create_chat_completion(
            workspace_uid="test",
            messages=[{"role": "user", "content": "test"}],
        )

        assert result == ""  # Empty response should return empty string