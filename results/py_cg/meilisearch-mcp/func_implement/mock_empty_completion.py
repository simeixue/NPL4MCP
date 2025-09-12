# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.TestChatTools.test_empty_chat_response.mock_empty_completion
# lines: 168-170
        def mock_empty_completion(*args, **kwargs):
            # Return empty chunks
            return iter([])