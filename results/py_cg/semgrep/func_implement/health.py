# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.health
# lines: 436-438
async def health(request: Request) -> JSONResponse:
    """Health check endpoint"""
    return JSONResponse({"status": "ok", "version": __version__})