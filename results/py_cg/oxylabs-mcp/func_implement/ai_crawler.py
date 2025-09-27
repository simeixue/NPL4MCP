# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.ai_crawler
# lines: 89-94
def ai_crawler(mock_schema):
    mock_crawler = MagicMock()
    mock_crawler.generate_schema.return_value = mock_schema

    with patch("oxylabs_mcp.tools.ai_studio.AiCrawler", return_value=mock_crawler):
        yield mock_crawler