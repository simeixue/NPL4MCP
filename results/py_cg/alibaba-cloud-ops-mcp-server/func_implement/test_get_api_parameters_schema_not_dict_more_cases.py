# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_schema_not_dict_more_cases
# lines: 206-221
def test_get_api_parameters_schema_not_dict_more_cases(mock_get_meta):
    """测试get_api_parameters中更多非dict类型的schema"""
    api_meta = {
        'parameters': [
            {'name': 'foo', 'in': 'query', 'schema': 'string'},  # 字符串
            {'name': 'bar', 'in': 'query', 'schema': 123},       # 数字
            {'name': 'baz', 'in': 'query', 'schema': []},        # 列表
            {'name': 'qux', 'in': 'query', 'schema': None},      # None
        ]
    }
    mock_get_meta.return_value = (api_meta, '2014-05-26')
    params = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances')
    assert 'foo' in params
    assert 'bar' in params
    assert 'baz' in params
    assert 'qux' in params