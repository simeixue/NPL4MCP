# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.browser_agent
# lines: 107-112
def browser_agent(mock_schema):
    mock_browser_agent = MagicMock()
    mock_browser_agent.generate_schema.return_value = mock_schema

    with patch("oxylabs_mcp.tools.ai_studio.BrowserAgent", return_value=mock_browser_agent):
        yield mock_browser_agent