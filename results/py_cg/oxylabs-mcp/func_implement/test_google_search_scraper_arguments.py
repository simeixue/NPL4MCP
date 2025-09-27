# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_scraper_tools.py
# module: tests.integration.test_scraper_tools
# qname: tests.integration.test_scraper_tools.test_google_search_scraper_arguments
# lines: 68-90
async def test_google_search_scraper_arguments(
    mcp: FastMCP,
    request_data: Request,
    response_data: str,
    arguments: dict,
    expectation,
    expected_result: str,
    oxylabs_client: AsyncMock,
):
    mock_response = Response(200, content=json.dumps(response_data), request=request_data)
    oxylabs_client.post.return_value = mock_response

    with expectation:
        result = await mcp._call_tool("google_search_scraper", arguments=arguments)

        assert oxylabs_client.post.call_args.kwargs == {
            "json": {
                "source": "google_search",
                "parse": True,
                **prepare_expected_arguments(arguments),
            }
        }
        assert result.content == [TextContent(type="text", text=expected_result)]