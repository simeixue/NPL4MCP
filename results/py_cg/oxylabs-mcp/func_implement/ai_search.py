# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.ai_search
# lines: 116-120
def ai_search():
    mock_ai_search = MagicMock()

    with patch("oxylabs_mcp.tools.ai_studio.AiSearch", return_value=mock_ai_search):
        yield mock_ai_search