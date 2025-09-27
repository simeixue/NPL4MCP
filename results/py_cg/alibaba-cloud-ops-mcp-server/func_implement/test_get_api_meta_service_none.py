# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_meta_service_none
# lines: 48-51
def test_get_api_meta_service_none(mock_get_std, mock_get_ver):
    with pytest.raises(Exception) as e:
        api_meta_client.ApiMetaClient.get_api_meta('ecs', 'DescribeInstances')
    assert 'InvalidServiceName' in str(e.value)