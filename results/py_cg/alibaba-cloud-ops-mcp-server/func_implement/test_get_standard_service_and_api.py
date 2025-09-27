# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_standard_service_and_api
# lines: 28-36
def test_get_standard_service_and_api(mock_get):
    # 1st call: GetProductList, 2nd call: GetApiOverview
    mock_get.return_value.json.side_effect = [
        [{"code": "ecs", "defaultVersion": "2014-05-26"}],
        {"apis": {"DescribeInstances": {}}}
    ]
    service, api = api_meta_client.ApiMetaClient.get_standard_service_and_api('ecs', 'DescribeInstances', '2014-05-26')
    assert service == 'ecs'
    assert api == 'DescribeInstances'