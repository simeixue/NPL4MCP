# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.server_lifespan
# lines: 328-338
async def server_lifespan(_server: FastMCP) -> AsyncIterator[SemgrepContext]:
    """Manage server startup and shutdown lifecycle."""
    # Initialize resources on startup with tracing
    # MCP requires Pro Engine
    with start_tracing("mcp-python-server") as span:
        context = await mk_context(top_level_span=span)

        try:
            yield context
        finally:
            context.shutdown()