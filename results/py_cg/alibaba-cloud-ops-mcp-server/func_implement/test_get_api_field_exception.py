# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_field_exception
# lines: 109-111
def test_get_api_field_exception(mock_get_meta):
    val = api_meta_client.ApiMetaClient.get_api_field('parameters', 'ecs', 'DescribeInstances', default='d')
    assert val == 'd'