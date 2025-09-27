# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/__init__.py
# module: src.oxylabs_mcp.__init__
# qname: src.oxylabs_mcp.__init__.main
# lines: 45-60
def main() -> None:
    """Start the MCP server."""
    logging.getLogger("oxylabs_mcp").setLevel(settings.LOG_LEVEL)

    params: dict[str, Any] = {}

    if settings.MCP_TRANSPORT == "streamable-http":
        params["host"] = settings.MCP_HOST
        params["port"] = settings.PORT or settings.MCP_PORT
        params["log_level"] = settings.LOG_LEVEL
        params["stateless_http"] = settings.MCP_STATELESS_HTTP

    mcp.run(
        settings.MCP_TRANSPORT,
        **params,
    )