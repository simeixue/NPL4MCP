# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_response_from_pop_api_success
# lines: 6-10
def test_get_response_from_pop_api_success(mock_get):
    mock_get.return_value.json.return_value = [{"code": "ecs", "defaultVersion": "2014-05-26", "style": "RPC"}]
    data = api_meta_client.ApiMetaClient.get_response_from_pop_api('GetProductList')
    assert isinstance(data, list)
    assert data[0]["code"] == "ecs"