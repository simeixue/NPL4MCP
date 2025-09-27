# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/__init__.py
# module: src.mcp_server_motherduck.__init__
# qname: src.mcp_server_motherduck.__init__.main.arun
# lines: 178-180
        async def arun():
            async with stdio_server() as (read_stream, write_stream):
                await app.run(read_stream, write_stream, init_opts)