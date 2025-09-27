# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_tool_function_with_signature_required
# lines: 47-57
def test_create_tool_function_with_signature_required():
    api_meta, _ = fake_api_meta()
    schemas = api_tools._create_function_schemas('ecs', 'DescribeInstances', api_meta)
    fields = schemas['DescribeInstances']
    func = api_tools._create_tool_function_with_signature('ecs', 'DescribeInstances', fields, 'desc')
    # 检查参数名、类型、注释和default存在
    for name, (typ, field_info) in fields.items():
        param = func.__signature__.parameters[name]
        assert param.name == name
        assert param.annotation == typ
        assert hasattr(param, 'default')