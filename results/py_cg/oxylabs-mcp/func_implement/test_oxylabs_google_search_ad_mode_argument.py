# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_scraper_tools.py
# module: tests.integration.test_scraper_tools
# qname: tests.integration.test_scraper_tools.test_oxylabs_google_search_ad_mode_argument
# lines: 101-114
async def test_oxylabs_google_search_ad_mode_argument(
    mcp: FastMCP,
    request_data: Request,
    ad_mode: bool,
    expected_result: dict[str, Any],
    oxylabs_client: AsyncMock,
):
    arguments = {"query": "Iphone 16", "ad_mode": ad_mode}
    mock_response = Response(200, content=json.dumps('{"data": "value"}'), request=request_data)
    oxylabs_client.post.return_value = mock_response

    await mcp._call_tool("google_search_scraper", arguments=arguments)
    assert oxylabs_client.post.call_args.kwargs == {"json": expected_result}
    assert oxylabs_client.post.await_args.kwargs["json"] == expected_result