# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_field_default_value
# lines: 252-256
def test_get_api_field_default_value(mock_get_meta):
    # 模拟 get_api_meta 返回无 field_type 的数据
    mock_get_meta.return_value = ({}, '2014-05-26')
    val = api_meta_client.ApiMetaClient.get_api_field('parameters', 'ecs', 'DescribeInstances', default='default_val')
    assert val == 'default_val'