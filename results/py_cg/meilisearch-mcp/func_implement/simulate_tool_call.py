# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_chat.py
# module: tests.test_chat
# qname: tests.test_chat.simulate_tool_call
# lines: 63-83
async def simulate_tool_call(server, tool_name, arguments=None):
    """Simulate a tool call directly on the server"""
    handlers = {}

    # Get the tool handler
    @server.server.call_tool()
    async def handle_call_tool(name, arguments_=None):
        pass

    # The handler is registered, now call it directly
    result = await server._setup_handlers.__code__.co_consts[1](tool_name, arguments)

    # Actually call the handler through the server's method
    handler_func = None
    for name, obj in server.__class__.__dict__.items():
        if hasattr(obj, "__name__") and obj.__name__ == "handle_call_tool":
            handler_func = obj
            break

    # Call the actual handle_call_tool method
    return await server._MeilisearchMCPServer__handle_call_tool(tool_name, arguments)