# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/__init__.py
# module: src.mcp_server_motherduck.__init__
# qname: src.mcp_server_motherduck.__init__.main.handle_streamable_http
# lines: 133-136
        async def handle_streamable_http(
            scope: Scope, receive: Receive, send: Send
        ) -> None:
            await session_manager.handle_request(scope, receive, send)