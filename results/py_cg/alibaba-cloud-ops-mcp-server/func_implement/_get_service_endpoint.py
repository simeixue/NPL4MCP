# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._get_service_endpoint
# lines: 50-78
def _get_service_endpoint(service: str, region_id: str):
    region_id = region_id.lower()

    # Prioritizing central service endpoints
    central = CENTRAL_SERVICE_ENDPOINTS.get(service)
    if central:
        if settings.env == 'international':
            return central['InternationalEndpoint']
        elif region_id in central.get('DomesticRegion', []) or settings.env == 'domestic':
            return central['DomesticEndpoint']
        else:
            return central['InternationalEndpoint']

    # Determine whether to use regional endpoints
    if service in REGION_ENDPOINT_SERVICE:
        return f'{service}.{region_id}.aliyuncs.com'

    if service in DOUBLE_ENDPOINT_SERVICE:
        not_in_central = region_id not in DOUBLE_ENDPOINT_SERVICE[service]
        if not_in_central:
            return f'{service}.{region_id}.aliyuncs.com'
        else:
            return f'{service}.aliyuncs.com'

    if service in CENTRAL_SERVICE:
        return f'{service}.aliyuncs.com'

    # Default
    return f'{service}.{region_id}.aliyuncs.com'