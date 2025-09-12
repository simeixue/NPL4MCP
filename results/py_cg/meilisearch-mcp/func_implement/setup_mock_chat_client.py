# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.setup_mock_chat_client
# lines: 15-60
def setup_mock_chat_client(server):
    """Mock the Meilisearch client for chat-related methods"""
    # Create a mock client with chat methods
    mock_client = MagicMock()

    # Mock create_chat_completion to return an iterator
    def mock_chat_completion(*args, **kwargs):
        # Simulate streaming response chunks
        chunks = [
            {"choices": [{"delta": {"content": "This is "}}]},
            {"choices": [{"delta": {"content": "a test "}}]},
            {"choices": [{"delta": {"content": "response."}}]},
        ]
        for chunk in chunks:
            yield chunk

    mock_client.create_chat_completion = mock_chat_completion

    # Mock get_chat_workspaces
    mock_client.get_chat_workspaces.return_value = {
        "results": [
            {"uid": "workspace1", "name": "Customer Support"},
            {"uid": "workspace2", "name": "Documentation"},
        ],
        "limit": 10,
        "offset": 0,
        "total": 2,
    }

    # Mock get_chat_workspace_settings
    mock_client.get_chat_workspace_settings.return_value = {
        "model": "gpt-3.5-turbo",
        "indexUids": ["products", "docs"],
        "temperature": 0.7,
    }

    # Mock update_chat_workspace_settings
    mock_client.update_chat_workspace_settings.return_value = {
        "model": "gpt-4",
        "indexUids": ["products", "docs"],
        "temperature": 0.5,
    }

    # Replace the chat manager's client
    server.chat_manager.client = mock_client
    return server