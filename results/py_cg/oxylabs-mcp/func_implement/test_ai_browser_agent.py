# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_ai_studio_tools.py
# module: tests.integration.test_ai_studio_tools
# qname: tests.integration.test_ai_studio_tools.test_ai_browser_agent
# lines: 116-149
async def test_ai_browser_agent(
    mcp: FastMCP,
    request_data: Request,
    response_data: str,
    arguments: dict,
    expectation,
    expected_result: str,
    oxylabs_client: AsyncMock,
    browser_agent: AsyncMock,
):
    mock_result = MagicMock()
    mock_data = SimpleSchema(title="Title", price=0.0)
    mock_result.data = mock_data
    browser_agent.run_async = AsyncMock(return_value=mock_result)

    arguments = {"task_prompt": "Scrape price and title", **arguments}

    with expectation:
        result = await mcp._call_tool("ai_browser_agent", arguments=arguments)

        assert result.content == [
            TextContent(type="text", text=json.dumps({"data": mock_data.model_dump()}))
        ]

        default_args = {
            "geo_location": None,
            "output_format": "markdown",
            "schema": None,
            "user_prompt": arguments["task_prompt"],
        }
        del arguments["task_prompt"]
        default_args = {k: v for k, v in default_args.items() if k not in arguments}

        browser_agent.run_async.assert_called_once_with(**default_args, **arguments)