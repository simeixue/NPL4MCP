# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_create_chat_completion
# lines: 88-103
    async def test_create_chat_completion(self, setup_mock_chat_client):
        """Test creating a chat completion"""
        server = setup_mock_chat_client

        # Simulate the tool call
        result = await server.chat_manager.create_chat_completion(
            workspace_uid="test-workspace",
            messages=[
                {"role": "user", "content": "What is Meilisearch?"},
            ],
            model="gpt-3.5-turbo",
            stream=True,
        )

        # The result should be the combined response
        assert result == "This is a test response."