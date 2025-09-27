# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_all_service_info
# lines: 305-314
def test_get_all_service_info(mock_get):
    mock_get.return_value.json.return_value = [
        {"code": "ecs", "name": "Elastic Compute Service"},
        {"code": "rds", "name": "Relational Database Service"}
    ]
    result = api_meta_client.ApiMetaClient.get_all_service_info()
    assert result == [
        {"code": "ecs", "name": "Elastic Compute Service"},
        {"code": "rds", "name": "Relational Database Service"}
    ]