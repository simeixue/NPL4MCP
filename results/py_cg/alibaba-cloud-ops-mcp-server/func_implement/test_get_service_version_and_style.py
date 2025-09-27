# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_service_version_and_style
# lines: 20-25
def test_get_service_version_and_style(mock_get):
    mock_get.return_value.json.return_value = [{"code": "ecs", "defaultVersion": "2014-05-26", "style": "RPC"}]
    v = api_meta_client.ApiMetaClient.get_service_version('ecs')
    s = api_meta_client.ApiMetaClient.get_service_style('ecs')
    assert v == "2014-05-26"
    assert s == "RPC"