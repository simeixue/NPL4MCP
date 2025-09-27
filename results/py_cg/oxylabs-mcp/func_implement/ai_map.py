# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.ai_map
# lines: 124-128
def ai_map():
    mock_ai_map = MagicMock()

    with patch("oxylabs_mcp.tools.ai_studio.AiMap", return_value=mock_ai_map):
        yield mock_ai_map