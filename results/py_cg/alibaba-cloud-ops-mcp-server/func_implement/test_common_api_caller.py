# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_common_api_caller
# lines: 363-368
def test_common_api_caller(mock_call):
    import alibaba_cloud_ops_mcp_server.tools.common_api_tools as ca
    fn = ca.tools[3]  # CommonAPICaller
    mock_call.return_value = {'result': 'ok'}
    result = fn('ecs', 'DescribeInstances', {'foo': 'bar'})
    assert result == {'result': 'ok'}