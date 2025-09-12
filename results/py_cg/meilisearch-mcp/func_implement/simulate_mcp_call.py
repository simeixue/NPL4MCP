# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.simulate_mcp_call
# lines: 42-56
async def simulate_mcp_call(
    server: MeilisearchMCPServer, tool_name: str, arguments: Dict[str, Any] = None
) -> List[Any]:
    """Simulate an MCP client call to the server"""
    handler = server.server.request_handlers.get(CallToolRequest)
    if not handler:
        raise RuntimeError("No call_tool handler found")

    request = CallToolRequest(
        method="tools/call",
        params=CallToolRequestParams(name=tool_name, arguments=arguments or {}),
    )

    result = await handler(request)
    return result.root.content