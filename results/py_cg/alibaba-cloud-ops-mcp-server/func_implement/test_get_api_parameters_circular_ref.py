# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_circular_ref
# lines: 93-106
def test_get_api_parameters_circular_ref(mock_get_meta):
    # 测试循环引用
    api_meta = {
        'parameters': [
            {'name': 'foo', 'in': 'query', 'schema': {'type': 'string', '$ref': '#/defs/foo'}}
        ]
    }
    # get_ref_api_meta返回带$ref的结构，模拟循环
    def fake_get_ref(data, service, version):
        return {'$ref': '#/defs/foo'}
    with patch.object(api_meta_client.ApiMetaClient, 'get_ref_api_meta', side_effect=fake_get_ref):
        mock_get_meta.return_value = (api_meta, '2014-05-26')
        params = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances')
        assert 'foo' in params