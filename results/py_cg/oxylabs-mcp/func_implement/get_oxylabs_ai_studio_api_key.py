# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils.get_oxylabs_ai_studio_api_key
# lines: 187-198
def get_oxylabs_ai_studio_api_key() -> str | None:
    """Extract the Oxylabs AI Studio API key."""
    if settings.MCP_TRANSPORT == "streamable-http":
        request_headers = dict(get_context().request_context.request.headers)  # type: ignore[union-attr]
        ai_studio_api_key = request_headers.get(AI_STUDIO_API_KEY_HEADER.lower())
        if not ai_studio_api_key:
            query_params = get_context().request_context.request.query_params  # type: ignore[union-attr]
            ai_studio_api_key = query_params.get(AI_STUDIO_API_KEY_QUERY_PARAM)
    else:
        ai_studio_api_key = os.getenv(AI_STUDIO_API_KEY_ENV)

    return ai_studio_api_key