# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_function_schemas_ecs_list_parameters
# lines: 136-159
def test_create_function_schemas_ecs_list_parameters():
    # 测试ECS服务的特殊参数处理
    api_meta = {
        'parameters': [
            {'name': 'InstanceIds', 'schema': {'type': 'string', 'description': '实例ID列表', 'example': '["i-123", "i-456"]', 'required': True}},
            {'name': 'SecurityGroupIds', 'schema': {'type': 'string', 'description': '安全组ID列表', 'example': '["sg-123", "sg-456"]', 'required': False}},
            {'name': 'NormalParam', 'schema': {'type': 'string', 'description': '普通参数', 'example': 'test', 'required': False}},
        ],
        'methods': ['get'],
        'path': '/test',
        'summary': '测试API'
    }
    
    # 测试ECS服务
    schemas = api_tools._create_function_schemas('ecs', 'DescribeInstances', api_meta)
    assert schemas['DescribeInstances']['InstanceIds'][0] == list
    assert schemas['DescribeInstances']['SecurityGroupIds'][0] == list
    assert schemas['DescribeInstances']['NormalParam'][0] == str
    
    # 测试非ECS服务
    schemas = api_tools._create_function_schemas('rds', 'DescribeInstances', api_meta)
    assert schemas['DescribeInstances']['InstanceIds'][0] == str
    assert schemas['DescribeInstances']['SecurityGroupIds'][0] == str
    assert schemas['DescribeInstances']['NormalParam'][0] == str