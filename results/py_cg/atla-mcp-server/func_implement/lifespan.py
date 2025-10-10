# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/atla-mcp-server/atla_mcp_server/server.py
# module: atla_mcp_server.server
# qname: atla_mcp_server.server.app_factory.lifespan
# lines: 246-253
    async def lifespan(_: FastMCP) -> AsyncIterator[MCPState]:
        async with AsyncAtla(
            api_key=atla_api_key,
            default_headers={
                "X-Atla-Source": "mcp-server",
            },
        ) as client:
            yield MCPState(atla_client=client)