# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils.get_oxylabs_auth
# lines: 170-184
def get_oxylabs_auth() -> tuple[str | None, str | None]:
    """Extract the Oxylabs credentials."""
    if settings.MCP_TRANSPORT == "streamable-http":
        request_headers = dict(get_context().request_context.request.headers)  # type: ignore[union-attr]
        username = request_headers.get(USERNAME_HEADER.lower())
        password = request_headers.get(PASSWORD_HEADER.lower())
        if not username or not password:
            query_params = get_context().request_context.request.query_params  # type: ignore[union-attr]
            username = query_params.get(USERNAME_QUERY_PARAM)
            password = query_params.get(PASSWORD_QUERY_PARAM)
    else:
        username = os.environ.get(USERNAME_ENV)
        password = os.environ.get(PASSWORD_ENV)

    return username, password