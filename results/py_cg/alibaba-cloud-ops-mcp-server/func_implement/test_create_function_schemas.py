# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_function_schemas
# lines: 30-36
def test_create_function_schemas():
    api_meta, _ = fake_api_meta()
    schemas = api_tools._create_function_schemas('ecs', 'DescribeInstances', api_meta)
    assert 'DescribeInstances' in schemas
    assert 'InstanceId' in schemas['DescribeInstances']
    assert schemas['DescribeInstances']['InstanceId'][0] == str
    assert schemas['DescribeInstances']['Ids'][0] == list