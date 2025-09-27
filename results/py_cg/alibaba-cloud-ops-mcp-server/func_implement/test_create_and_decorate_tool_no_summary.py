# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_and_decorate_tool_no_summary
# lines: 85-89
def test_create_and_decorate_tool_no_summary():
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools.ApiMetaClient.get_api_meta', return_value=fake_api_meta(no_summary=True)):
        mcp = DummyMCP()
        fn = api_tools._create_and_decorate_tool(mcp, 'ecs', 'DescribeInstances')
        assert callable(fn)