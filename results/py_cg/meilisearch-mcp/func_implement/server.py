# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.server
# lines: 10-11
def server():
    return MeilisearchMCPServer(url="http://localhost:7700", api_key="test_key")