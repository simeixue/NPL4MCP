# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_server.py
# module: mcp_hydrolix.mcp_server
# qname: mcp_hydrolix.mcp_server.health_check
# lines: 76-88
async def health_check(request: Request) -> PlainTextResponse:
    """Health check endpoint for monitoring server status.

    Returns OK if the server is running and can connect to Hydrolix.
    """
    try:
        # Try to create a client connection to verify query-head connectivity
        client = create_hydrolix_client()
        version = client.server_version
        return PlainTextResponse(f"OK - Connected to Hydrolix compatible with ClickHouse {version}")
    except Exception as e:
        # Return 503 Service Unavailable if we can't connect to Hydrolix
        return PlainTextResponse(f"ERROR - Cannot connect to Hydrolix: {str(e)}", status_code=503)