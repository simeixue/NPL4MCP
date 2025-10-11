# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/server.py
# module: src.fibery_mcp_server.server
# qname: src.fibery_mcp_server.server.main._run
# lines: 53-67
    async def _run() -> None:
        async with mcp.stdio_server() as (read_stream, write_stream):
            server = await serve(parsed_fibery_host, fibery_api_token)
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="Fibery MCP",
                    server_version="0.0.1",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )