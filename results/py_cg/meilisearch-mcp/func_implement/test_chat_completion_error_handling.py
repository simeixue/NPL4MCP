# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_chat_completion_error_handling
# lines: 144-160
    async def test_chat_completion_error_handling(self, server):
        """Test error handling in chat completion"""
        # Mock the client to raise an error
        server.chat_manager.client = MagicMock()
        # Create a mock request object for the error with proper JSON text
        mock_request = MagicMock()
        mock_request.status_code = 400
        mock_request.text = '{"message": "Chat feature not enabled", "code": "chat_not_enabled", "type": "invalid_request", "link": "https://docs.meilisearch.com/errors#chat_not_enabled"}'
        server.chat_manager.client.create_chat_completion.side_effect = (
            MeilisearchApiError("Chat feature not enabled", mock_request)
        )

        with pytest.raises(MeilisearchApiError):
            await server.chat_manager.create_chat_completion(
                workspace_uid="test",
                messages=[{"role": "user", "content": "test"}],
            )