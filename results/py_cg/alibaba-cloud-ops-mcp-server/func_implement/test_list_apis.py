# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_list_apis
# lines: 347-352
def test_list_apis(mock_get):
    import alibaba_cloud_ops_mcp_server.tools.common_api_tools as ca
    fn = ca.tools[1]  # ListAPIs
    mock_get.return_value = ['DescribeInstances', 'StartInstance']
    result = fn('ecs')
    assert result == ['DescribeInstances', 'StartInstance']