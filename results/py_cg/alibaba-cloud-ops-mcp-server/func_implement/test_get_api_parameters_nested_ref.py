# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_nested_ref
# lines: 259-275
def test_get_api_parameters_nested_ref(mock_get_meta):
    # 模拟嵌套 $ref
    api_meta = {
        'parameters': [
            {'name': 'foo', 'in': 'query', 'schema': {'$ref': '#/defs/A'}}
        ]
    }
    def fake_get_ref(data, service, version):
        if '#/defs/A' in data.get('$ref', ''):
            return {'properties': {'a': {'$ref': '#/defs/B'}}}
        elif '#/defs/B' in data.get('$ref', ''):
            return {'properties': {'b': {}}}
        return {}
    with patch.object(api_meta_client.ApiMetaClient, 'get_ref_api_meta', side_effect=fake_get_ref):
        mock_get_meta.return_value = (api_meta, '2014-05-26')
        params = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances')
        assert 'a' in params and 'b' in params  # 深层嵌套属性应被提取