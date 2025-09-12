# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.setup_mock_chat_client.mock_chat_completion
# lines: 21-29
    def mock_chat_completion(*args, **kwargs):
        # Simulate streaming response chunks
        chunks = [
            {"choices": [{"delta": {"content": "This is "}}]},
            {"choices": [{"delta": {"content": "a test "}}]},
            {"choices": [{"delta": {"content": "response."}}]},
        ]
        for chunk in chunks:
            yield chunk