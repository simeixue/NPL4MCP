# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_user_agent.py
# module: tests.test_user_agent
# qname: tests.test_user_agent.test_meilisearch_client_sets_custom_user_agent
# lines: 7-18
def test_meilisearch_client_sets_custom_user_agent():
    """Test that MeilisearchClient initializes with custom user agent"""
    with patch("src.meilisearch_mcp.client.Client") as mock_client:
        # Create a MeilisearchClient instance
        client = MeilisearchClient(url="http://localhost:7700", api_key="test_key")

        # Verify that Client was called with the correct parameters
        mock_client.assert_called_once_with(
            "http://localhost:7700",
            "test_key",
            client_agents=("meilisearch-mcp", f"v{__version__}"),
        )