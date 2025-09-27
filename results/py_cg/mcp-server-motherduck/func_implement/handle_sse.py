# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/__init__.py
# module: src.mcp_server_motherduck.__init__
# qname: src.mcp_server_motherduck.__init__.main.handle_sse
# lines: 87-92
        async def handle_sse(request):
            async with sse.connect_sse(
                request.scope, request.receive, request._send
            ) as (read_stream, write_stream):
                await app.run(read_stream, write_stream, init_opts)
            return Response()