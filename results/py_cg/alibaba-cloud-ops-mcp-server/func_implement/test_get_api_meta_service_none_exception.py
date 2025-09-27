# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_meta_service_none_exception
# lines: 190-194
def test_get_api_meta_service_none_exception(mock_pop_api, mock_get_std, mock_get_ver):
    """测试get_api_meta方法中service_standard为None时抛出异常"""
    with pytest.raises(Exception) as e:
        api_meta_client.ApiMetaClient.get_api_meta('ecs', 'DescribeInstances')
    assert 'InvalidServiceName' in str(e.value)