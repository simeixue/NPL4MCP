# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._create_and_decorate_tool
# lines: 256-265
def _create_and_decorate_tool(mcp: FastMCP, service: str, api: str):
    """Create a tool function for an AlibabaCloud openapi."""
    api_meta, _ = ApiMetaClient.get_api_meta(service, api)
    fields = _create_function_schemas(service, api, api_meta).get(api, {})
    description = api_meta.get('summary', '')
    dynamic_lambda = _create_tool_function_with_signature(service, api, fields, description)
    function_name = f'{service.upper()}_{api}'
    decorated_function = mcp.tool(name=function_name)(dynamic_lambda)

    return decorated_function