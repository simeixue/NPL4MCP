# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_response_from_api_meta_empty
# lines: 61-64
def test_get_response_from_api_meta_empty(mock_get_meta):
    prop, ver = api_meta_client.ApiMetaClient.get_response_from_api_meta('ecs', 'DescribeInstances')
    assert prop == {}
    assert ver == '2014-05-26'