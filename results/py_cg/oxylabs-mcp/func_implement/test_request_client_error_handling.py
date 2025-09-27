# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_server.py
# module: tests.integration.test_server
# qname: tests.integration.test_server.test_request_client_error_handling
# lines: 116-130
async def test_request_client_error_handling(
    mcp: FastMCP,
    request_data: Request,
    oxylabs_client: AsyncMock,
    tool: str,
    arguments: dict,
    exception: Exception,
    expected_text: str,
):
    oxylabs_client.post.side_effect = [exception]
    oxylabs_client.get.side_effect = [exception]

    result = await mcp._call_tool(tool, arguments=arguments)

    assert result.content[0].text == expected_text