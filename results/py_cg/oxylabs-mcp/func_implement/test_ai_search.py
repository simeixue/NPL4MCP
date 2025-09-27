# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_ai_studio_tools.py
# module: tests.integration.test_ai_studio_tools
# qname: tests.integration.test_ai_studio_tools.test_ai_search
# lines: 163-199
async def test_ai_search(
    mcp: FastMCP,
    request_data: Request,
    response_data: str,
    arguments: dict,
    expectation,
    expected_result: str,
    oxylabs_client: AsyncMock,
    ai_search: AsyncMock,
):
    mock_result = AiSearchJob(
        run_id="123",
        data=[SearchResult(url="url", title="title", description="description", content=None)],
    )
    ai_search.search_async = AsyncMock(return_value=mock_result)

    arguments = {**arguments}
    if "url" in arguments:
        del arguments["url"]
        arguments["query"] = "Sample query"

    with expectation:
        result = await mcp._call_tool("ai_search", arguments=arguments)

        assert result.content == [
            TextContent(type="text", text=json.dumps({"data": [mock_result.data[0].model_dump()]}))
        ]

        default_args = {
            "limit": 10,
            "render_javascript": False,
            "return_content": False,
            "geo_location": None,
        }
        default_args = {k: v for k, v in default_args.items() if k not in arguments}

        ai_search.search_async.assert_called_once_with(**default_args, **arguments)