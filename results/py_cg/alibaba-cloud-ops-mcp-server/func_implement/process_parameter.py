# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._create_function_schemas.process_parameter
# lines: 163-184
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