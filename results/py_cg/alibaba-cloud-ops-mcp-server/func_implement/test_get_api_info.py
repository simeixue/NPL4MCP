# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_get_api_info
# lines: 355-360
def test_get_api_info(mock_get):
    import alibaba_cloud_ops_mcp_server.tools.common_api_tools as ca
    fn = ca.tools[2]  # GetAPIInfo
    mock_get.return_value = ({'parameters': [{'name': 'foo'}]}, '2014-05-26')
    result = fn('ecs', 'DescribeInstances')
    assert result == [{'name': 'foo'}]