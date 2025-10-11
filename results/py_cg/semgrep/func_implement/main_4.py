# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.main
# lines: 468-490
def main(transport: str, semgrep_path: str | None) -> None:
    """Entry point for the MCP server

    Supports stdio, streamable-http, and sse transports.
    For stdio, it will read from stdin and write to stdout.
    For streamable-http and sse, it will start an HTTP server on port 8000.
    """
    logging.info(
        f"Starting Semgrep MCP server v{__version__}, Semgrep version v{get_semgrep_version()}"
    )

    # Set the executable path in case it's manually specified.
    if semgrep_path:
        set_semgrep_executable(semgrep_path)

    if transport == "stdio":
        mcp.run(transport="stdio")
    elif transport == "streamable-http":
        mcp.run(transport="streamable-http")
    elif transport == "sse":
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Invalid transport: {transport}")