# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_params_in_and_ref
# lines: 75-90
def test_get_api_parameters_params_in_and_ref(mock_get_meta):
    # 测试params_in过滤和递归ref
    api_meta = {
        'parameters': [
            {'name': 'foo', 'in': 'query', 'schema': {'type': 'string'}},
            {'name': 'bar', 'in': 'body', 'schema': {'type': 'string', '$ref': '#/defs/bar'}}
        ]
    }
    # get_ref_api_meta返回递归结构
    with patch.object(api_meta_client.ApiMetaClient, 'get_ref_api_meta', return_value={'properties': {'baz': {}}}):
        mock_get_meta.return_value = (api_meta, '2014-05-26')
        params = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances', params_in='query')
        assert params == ['foo']
        # 测试递归ref
        params2 = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances')
        assert 'baz' in params2