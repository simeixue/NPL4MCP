# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_user_agent.py
# module: tests.test_user_agent
# qname: tests.test_user_agent.test_user_agent_includes_correct_version
# lines: 21-33
def test_user_agent_includes_correct_version():
    """Test that the user agent includes the correct version from __version__.py"""
    with patch("src.meilisearch_mcp.client.Client") as mock_client:
        client = MeilisearchClient()

        # Extract the client_agents parameter from the call
        call_args = mock_client.call_args
        client_agents = call_args[1]["client_agents"]

        # Verify format and version
        assert client_agents[0] == "meilisearch-mcp"
        assert client_agents[1] == "v0.5.0"
        assert client_agents[1] == f"v{__version__}"