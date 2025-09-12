# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/bicscan-mcp/src/bicscan_mcp/server.py
# module: src.bicscan_mcp.server
# qname: src.bicscan_mcp.server.main
# lines: 110-113
async def main() -> None:
    """Run the MCP BICScan server."""
    # Import here to avoid issues with event loops
    await mcp.run_stdio_async()