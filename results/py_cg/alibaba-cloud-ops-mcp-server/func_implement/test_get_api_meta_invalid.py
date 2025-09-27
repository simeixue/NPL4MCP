# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_meta_invalid
# lines: 39-44
def test_get_api_meta_invalid(mock_get):
    # 1st call: GetProductList returns empty list
    mock_get.return_value.json.return_value = []
    with pytest.raises(Exception) as e:
        api_meta_client.ApiMetaClient.get_api_meta('notexist', 'api')
    assert 'InvalidServiceName' in str(e.value) or 'object has no attribute' in str(e.value)