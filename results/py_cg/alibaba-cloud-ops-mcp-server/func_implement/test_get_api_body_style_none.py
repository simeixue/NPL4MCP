# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_body_style_none
# lines: 113-121
def test_get_api_body_style_none():
    # get_api_field返回None
    with patch.object(api_meta_client.ApiMetaClient, 'get_api_field', return_value=None):
        val = api_meta_client.ApiMetaClient.get_api_body_style('ecs', 'DescribeInstances')
        assert val is None
    # get_api_field返回无STYLE参数
    with patch.object(api_meta_client.ApiMetaClient, 'get_api_field', return_value=[{'in': 'body'}]):
        val = api_meta_client.ApiMetaClient.get_api_body_style('ecs', 'DescribeInstances')
        assert val is None