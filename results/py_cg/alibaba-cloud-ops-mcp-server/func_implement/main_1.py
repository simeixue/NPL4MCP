# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/server.py
# module: src.alibaba_cloud_ops_mcp_server.server
# qname: src.alibaba_cloud_ops_mcp_server.server.main
# lines: 64-92
def main(transport: str, port: int, host: str, services: str, headers_credential_only: bool, env: str):
    # Create an MCP server
    mcp = FastMCP(
        name="alibaba-cloud-ops-mcp-server",
        port=port,
        host=host,
        stateless_http=True
    )
    if headers_credential_only:
        settings.headers_credential_only = headers_credential_only
    if env:
        settings.env = env
    if services:
        service_keys = [s.strip().lower() for s in services.split(",")]
        service_list = [(key, SUPPORTED_SERVICES_MAP.get(key, key)) for key in service_keys]
        set_custom_service_list(service_list)
        for tool in common_api_tools.tools:
            mcp.tool(tool)
    for tool in oos_tools.tools:
        mcp.tool(tool)
    for tool in cms_tools.tools:
        mcp.tool(tool)
    for tool in oss_tools.tools:
        mcp.tool(tool)
    api_tools.create_api_tools(mcp, config)

    # Initialize and run the server
    logger.debug(f'mcp server is running on {transport} mode.')
    mcp.run(transport=transport)