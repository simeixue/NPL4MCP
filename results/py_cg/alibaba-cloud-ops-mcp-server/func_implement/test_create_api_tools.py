# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_api_tools
# lines: 91-96
def test_create_api_tools():
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools._create_and_decorate_tool') as mock_create:
        mcp = DummyMCP()
        config = {'ecs': ['DescribeInstances', 'StartInstance'], 'rds': ['DescribeDBInstances']}
        api_tools.create_api_tools(mcp, config)
        assert mock_create.call_count == 3