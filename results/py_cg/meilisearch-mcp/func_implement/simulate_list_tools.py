# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.simulate_list_tools
# lines: 59-67
async def simulate_list_tools(server: MeilisearchMCPServer) -> List[Any]:
    """Simulate an MCP client request to list tools"""
    handler = server.server.request_handlers.get(ListToolsRequest)
    if not handler:
        raise RuntimeError("No list_tools handler found")

    request = ListToolsRequest(method="tools/list")
    result = await handler(request)
    return result.root.tools