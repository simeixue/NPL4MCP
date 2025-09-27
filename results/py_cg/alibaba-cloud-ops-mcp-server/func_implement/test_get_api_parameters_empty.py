# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_empty
# lines: 149-153
def test_get_api_parameters_empty():
    # parameters 为空
    with patch.object(api_meta_client.ApiMetaClient, 'get_api_meta', return_value=({'parameters': []}, '2014-05-26')):
        params = api_meta_client.ApiMetaClient.get_api_parameters('ecs', 'DescribeInstances')
        assert params == []