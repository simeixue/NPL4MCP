# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_ai_studio_tools.py
# module: tests.integration.test_ai_studio_tools
# qname: tests.integration.test_ai_studio_tools.test_ai_map
# lines: 247-277
async def test_ai_map(
    mcp: FastMCP,
    request_data: Request,
    response_data: str,
    arguments: dict,
    expectation,
    expected_result: str,
    oxylabs_client: AsyncMock,
    ai_map: AsyncMock,
):
    mock_result = MagicMock()
    mock_result.data = expected_result
    ai_map.map_async = AsyncMock(return_value=mock_result)

    arguments = {"user_prompt": "Scrape price and title", **arguments}

    with expectation:
        result = await mcp._call_tool("ai_map", arguments=arguments)

        assert result.content == [
            TextContent(type="text", text=json.dumps({"data": expected_result}))
        ]

        default_args = {
            "geo_location": None,
            "render_javascript": False,
            "return_sources_limit": 25,
        }
        default_args = {k: v for k, v in default_args.items() if k not in arguments}

        ai_map.map_async.assert_called_once_with(**default_args, **arguments)