# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils._get_default_headers
# lines: 126-141
def _get_default_headers() -> dict[str, str]:
    headers = {}
    if request_ctx := get_context().request_context:
        if client_params := request_ctx.session.client_params:
            client = f"oxylabs-mcp-{client_params.clientInfo.name}"
        else:
            client = "oxylabs-mcp"
    else:
        client = "oxylabs-mcp"

    bits, _ = architecture()
    sdk_type = f"{client}/{version('oxylabs-mcp')} ({python_version()}; {bits})"

    headers["x-oxylabs-sdk"] = sdk_type

    return headers