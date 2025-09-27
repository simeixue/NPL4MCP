# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_response_from_pop_api_keyerror
# lines: 134-139
def test_get_response_from_pop_api_keyerror(mock_get):
    # config 缺 key
    with patch.object(api_meta_client.ApiMetaClient, 'config', {'GetProductList': {}}):
        with pytest.raises(Exception) as e:
            api_meta_client.ApiMetaClient.get_response_from_pop_api('GetProductList')
        assert 'Failed to format path' in str(e.value)