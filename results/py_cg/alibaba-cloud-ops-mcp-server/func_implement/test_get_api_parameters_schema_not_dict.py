# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_schema_not_dict
# lines: 162-174
def test_get_api_parameters_schema_not_dict(mock_get):
    # get_api_meta返回的schema不是dict
    api_meta = {
        'parameters': [
            {'name': 'foo', 'in': 'query', 'schema': None},
            {'name': 'bar', 'in': 'query', 'schema': 'notadict'}
        ]
    }
    with patch.object(api_meta_client.ApiMetaClient, 'get_api_meta', return_value=(api_meta, '2014-05-26')):
        params = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances')
        # 两个参数都应该被返回
        assert 'foo' in params
        assert 'bar' in params