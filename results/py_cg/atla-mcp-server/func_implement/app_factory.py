# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/atla-mcp-server/atla_mcp_server/server.py
# module: atla_mcp_server.server
# qname: atla_mcp_server.server.app_factory
# lines: 242-259
def app_factory(atla_api_key: str) -> FastMCP:
    """Factory function to create an Atla MCP server with the given API key."""

    @asynccontextmanager
    async def lifespan(_: FastMCP) -> AsyncIterator[MCPState]:
        async with AsyncAtla(
            api_key=atla_api_key,
            default_headers={
                "X-Atla-Source": "mcp-server",
            },
        ) as client:
            yield MCPState(atla_client=client)

    mcp = FastMCP("Atla", lifespan=lifespan)
    mcp.tool()(evaluate_llm_response)
    mcp.tool()(evaluate_llm_response_on_multiple_criteria)

    return mcp