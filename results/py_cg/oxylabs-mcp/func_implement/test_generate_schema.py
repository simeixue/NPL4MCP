# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_ai_studio_tools.py
# module: tests.integration.test_ai_studio_tools
# qname: tests.integration.test_ai_studio_tools.test_generate_schema
# lines: 213-234
async def test_generate_schema(
    mcp: FastMCP,
    request_data: Request,
    response_data: str,
    arguments: dict,
    expectation,
    expected_result: str,
    oxylabs_client: AsyncMock,
    app_name: str,
    ai_crawler: AsyncMock,
    ai_scraper: AsyncMock,
    browser_agent: AsyncMock,
    mock_schema: dict,
):
    arguments = {"app_name": app_name, **arguments}

    with expectation:
        result = await mcp._call_tool("generate_schema", arguments=arguments)

        assert result.content == [TextContent(type="text", text=json.dumps({"data": mock_schema}))]

        locals()[app_name].generate_schema.assert_called_once_with(prompt=arguments["user_prompt"])