# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._create_function_schemas
# lines: 142-202
def _create_function_schemas(service, api, api_meta):
    schemas = {}
    schemas[api] = {}
    parameters = api_meta.get('parameters', [])

    required_params = []
    optional_params = []

    for parameter in parameters:
        name = parameter.get('name')
        # TODO 目前忽略了带'.'的参数
        if '.' in name:
            continue
        schema = parameter.get('schema', '')
        required = schema.get('required', False)

        if required:
            required_params.append(parameter)
        else:
            optional_params.append(parameter)

    def process_parameter(parameter):
        name = parameter.get('name')
        schema = parameter.get('schema', '')
        description = schema.get('description', '')
        example = schema.get('example', '')
        type_ = schema.get('type', '')
        description = f'{description} 参数类型: {type_},参数示例：{example}'
        required = schema.get('required', False)

        if service.lower() == 'ecs' and name in ECS_LIST_PARAMETERS and type_ == 'string':
            python_type = list
        else:
            python_type = type_map.get(type_, str)

        field_info = (
            python_type,
            field(
                default=None,
                metadata={'description': description, 'required': required}
            )
        )
        return name, field_info

    for parameter in required_params:
        name, field_info = process_parameter(parameter)
        schemas[api][name] = field_info

    for parameter in optional_params:
        name, field_info = process_parameter(parameter)
        schemas[api][name] = field_info

    if 'RegionId' not in schemas[api]:
        schemas[api]['RegionId'] = (
            str,
            field(
                default='cn-hangzhou',
                metadata={'description': '地域ID', 'required': False}
            )
        )
    return schemas