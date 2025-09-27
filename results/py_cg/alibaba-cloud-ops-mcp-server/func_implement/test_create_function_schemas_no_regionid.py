# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_function_schemas_no_regionid
# lines: 109-116
def test_create_function_schemas_no_regionid():
    api_meta = {
        'parameters': [
            {'name': 'foo', 'schema': {'type': 'string'}},
        ]
    }
    schemas = api_tools._create_function_schemas('ecs', 'TestApi', api_meta)
    assert 'RegionId' in schemas['TestApi']