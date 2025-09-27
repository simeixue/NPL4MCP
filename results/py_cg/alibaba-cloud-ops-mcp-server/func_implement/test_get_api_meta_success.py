# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_meta_success
# lines: 321-355
def test_get_api_meta_success(mock_pop_api, mock_get_std, mock_get_ver):
    """测试get_api_meta方法的正常成功路径，覆盖第90-91行"""
    # 模拟get_response_from_pop_api返回的API元数据
    mock_api_data = {
        'parameters': [
            {'name': 'InstanceIds', 'in': 'query', 'schema': {'type': 'string'}}
        ],
        'responses': {
            '200': {
                'schema': {
                    'properties': {
                        'Instances': {'type': 'array'}
                    }
                }
            }
        }
    }
    mock_pop_api.return_value = mock_api_data
    
    # 调用get_api_meta
    data, version = api_meta_client.ApiMetaClient.get_api_meta('ecs', 'DescribeInstances')
    
    # 验证返回值
    assert data == mock_api_data
    assert version == '2014-05-26'
    
    # 验证调用了正确的方法
    mock_get_ver.assert_called_once_with('ecs')
    mock_get_std.assert_called_once_with('ecs', 'DescribeInstances', '2014-05-26')
    mock_pop_api.assert_called_once_with(
        api_meta_client.ApiMetaClient.GET_API_INFO, 
        'ecs', 
        'DescribeInstances', 
        '2014-05-26'
    )