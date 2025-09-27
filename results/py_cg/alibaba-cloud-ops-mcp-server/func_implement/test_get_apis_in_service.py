# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_apis_in_service
# lines: 124-131
def test_get_apis_in_service(mock_get):
    # 第一次调用 get_service_version 需要 list，第二次 get_response_from_pop_api 需要 dict
    mock_get.return_value.json.side_effect = [
        [{"code": "ecs", "defaultVersion": "2014-05-26"}],  # for get_service_version
        {"apis": {"A": {}, "B": {}}}  # for get_response_from_pop_api
    ]
    apis = api_meta_client.ApiMetaClient.get_apis_in_service('ecs')
    assert set(apis) == {"A", "B"}