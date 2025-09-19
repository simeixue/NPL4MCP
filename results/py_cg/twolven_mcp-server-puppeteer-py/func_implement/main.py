# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.main
# lines: 246-254
async def main():
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )