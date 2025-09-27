# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._tools_api_call
# lines: 100-135
def _tools_api_call(service: str, api: str, parameters: dict, ctx: Context):
    service = service.lower()
    api_meta, _ = ApiMetaClient.get_api_meta(service, api)
    version = ApiMetaClient.get_service_version(service)
    method = 'POST' if api_meta.get('methods', [])[0] == 'post' else 'GET'
    path = api_meta.get('path', '/')
    style = ApiMetaClient.get_service_style(service)
    
    # Handling special parameter formats
    processed_parameters = parameters.copy()
    processed_parameters = {k: v for k, v in processed_parameters.items() if v is not None}
    if service == 'ecs':
        for param_name, param_value in parameters.items():
            if param_name in ECS_LIST_PARAMETERS and isinstance(param_value, list):
                processed_parameters[param_name] = json.dumps(param_value)
    
    req = open_api_models.OpenApiRequest(
        query=OpenApiUtilClient.query(processed_parameters)
    )
    params = open_api_models.Params(
        action=api,
        version=version,
        protocol='HTTPS',
        pathname=path,
        method=method,
        auth_type='AK',
        style=style,
        req_body_type='formData',
        body_type='json'
    )
    logger.info(f'Call API Request: Service: {service} API: {api} Method: {method} Parameters: {processed_parameters}')
    client = create_client(service, processed_parameters.get('RegionId', 'cn-hangzhou'))
    runtime = util_models.RuntimeOptions()
    resp = client.call_api(params, req, runtime)
    logger.info(f'Call API Response: {resp}')
    return resp