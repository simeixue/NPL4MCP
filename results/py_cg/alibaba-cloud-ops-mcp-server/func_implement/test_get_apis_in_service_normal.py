# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_apis_in_service_normal
# lines: 177-185
def test_get_apis_in_service_normal(mock_get):
    """测试get_apis_in_service方法正常返回API列表"""
    mock_get.return_value.json.side_effect = [
        [{"code": "ecs", "defaultVersion": "2014-05-26"}],  # for get_service_version
        {"apis": {"DescribeInstances": {}, "StartInstance": {}}}  # for get_response_from_pop_api
    ]
    apis = api_meta_client.ApiMetaClient.get_apis_in_service('ecs')
    assert set(apis) == {"DescribeInstances", "StartInstance"}
    assert len(apis) == 2