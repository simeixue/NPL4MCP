# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_response_from_api_meta_no_properties
# lines: 142-147
def test_get_response_from_api_meta_no_properties(mock_get_meta):
    # property_values 取不到属性
    with patch.dict('alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.__dict__', {'RESPONSES': 'responses', 'HTTP_SUCCESS_CODE': '200', 'SCHEMA': 'schema', 'PROPERTIES': 'properties'}):
        prop, ver = api_meta_client.ApiMetaClient.get_response_from_api_meta('ecs', 'DescribeInstances')
        assert prop == {}
        assert ver == '2014-05-26'