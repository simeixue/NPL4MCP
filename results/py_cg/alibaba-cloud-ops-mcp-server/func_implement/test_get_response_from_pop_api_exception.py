# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_response_from_pop_api_exception
# lines: 13-17
def test_get_response_from_pop_api_exception(mock_get):
    mock_get.side_effect = Exception('fail')
    with pytest.raises(Exception) as e:
        api_meta_client.ApiMetaClient.get_response_from_pop_api('GetProductList')
    assert 'Failed to get response' in str(e.value)