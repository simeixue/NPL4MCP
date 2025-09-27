# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_server.py
# module: tests.integration.test_server
# qname: tests.integration.test_server.test_default_headers_are_set
# lines: 39-63
async def test_default_headers_are_set(
    mcp: FastMCP,
    request_data: Request,
    oxylabs_client: AsyncMock,
    tool: str,
    arguments: dict,
):
    mock_response = Response(
        200,
        content=json.dumps(params.STR_RESPONSE),
        request=request_data,
    )

    oxylabs_client.post.return_value = mock_response
    oxylabs_client.get.return_value = mock_response

    await mcp._call_tool(tool, arguments=arguments)

    assert "x-oxylabs-sdk" in oxylabs_client.context_manager_call_kwargs["headers"]

    oxylabs_sdk_header = oxylabs_client.context_manager_call_kwargs["headers"]["x-oxylabs-sdk"]
    client_info, _ = oxylabs_sdk_header.split(maxsplit=1)

    client_info_pattern = re.compile(r"oxylabs-mcp-fake_cursor/(\d+)\.(\d+)\.(\d+)$")
    assert re.match(client_info_pattern, client_info)