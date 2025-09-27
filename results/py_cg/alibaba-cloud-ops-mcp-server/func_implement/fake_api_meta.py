# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.fake_api_meta
# lines: 10-22
def fake_api_meta(post=False, no_summary=False):
    meta = {
        'parameters': [
            {'name': 'InstanceId', 'schema': {'type': 'string', 'description': '实例ID', 'example': 'i-123', 'required': True}},
            {'name': 'RegionId', 'schema': {'type': 'string', 'description': '地域ID', 'example': 'cn-hangzhou', 'required': False}},
            {'name': 'Ids', 'schema': {'type': 'array', 'description': 'ID列表', 'example': '"[\"a\",\"b\"]"', 'required': False}},
        ],
        'methods': ['post'] if post else ['get'],
        'path': '/test',
    }
    if not no_summary:
        meta['summary'] = '测试API'
    return meta, '2023-01-01'