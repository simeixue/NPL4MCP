# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_ref_api_meta_keyerror
# lines: 68-72
def test_get_ref_api_meta_keyerror(mock_pop_api, mock_std):
    # ref_path指向不存在的key
    mock_pop_api.return_value = {'apis': {}}
    with pytest.raises(KeyError):
        api_meta_client.ApiMetaClient.get_ref_api_meta({'$ref': '#/notfound'}, 'ecs', '2014-05-26')