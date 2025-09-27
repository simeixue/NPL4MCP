# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/integration/test_server.py
# module: tests.integration.test_server
# qname: tests.integration.test_server.test_list_tools
# lines: 134-137
async def test_list_tools(mcp: FastMCP, transport: str):
    settings.MCP_TRANSPORT = transport
    tools = await mcp._mcp_list_tools()
    assert len(tools) == 10