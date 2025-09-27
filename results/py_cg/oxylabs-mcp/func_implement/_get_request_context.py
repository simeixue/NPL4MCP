# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils._get_request_context
# lines: 119-123
def _get_request_context(ctx: Context) -> RequestContext | None:  # type: ignore[type-arg]
    try:
        return ctx.request_context
    except ValueError:
        return None