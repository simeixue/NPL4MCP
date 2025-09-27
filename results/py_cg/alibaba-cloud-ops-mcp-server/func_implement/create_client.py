# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools.create_client
# lines: 81-88
def create_client(service: str, region_id: str) -> OpenApiClient:
    config = create_config()
    if isinstance(service, str):
        service = service.lower()
    endpoint = _get_service_endpoint(service, region_id.lower())
    config.endpoint = endpoint
    logger.info(f'Service Endpoint: {endpoint}')
    return OpenApiClient(config)