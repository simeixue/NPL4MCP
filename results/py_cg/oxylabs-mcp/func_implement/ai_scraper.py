# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.ai_scraper
# lines: 98-103
def ai_scraper(mock_schema):
    mock_scraper = MagicMock()
    mock_scraper.generate_schema.return_value = mock_schema

    with patch("oxylabs_mcp.tools.ai_studio.AiScraper", return_value=mock_scraper):
        yield mock_scraper