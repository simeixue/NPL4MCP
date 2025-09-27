# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_function_schemas_ignore_dot
# lines: 98-107
def test_create_function_schemas_ignore_dot():
    api_meta = {
        'parameters': [
            {'name': 'foo.bar', 'schema': {'type': 'string'}},
            {'name': 'baz', 'schema': {'type': 'string'}},
        ]
    }
    schemas = api_tools._create_function_schemas('ecs', 'TestApi', api_meta)
    assert 'foo.bar' not in schemas['TestApi']
    assert 'baz' in schemas['TestApi']