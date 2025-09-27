# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_apis_in_service_no_apis
# lines: 156-159
def test_get_apis_in_service_no_apis(mock_get):
    mock_get.return_value.json.return_value = {}
    with pytest.raises(KeyError):
        api_meta_client.ApiMetaClient.get_apis_in_service('ecs')