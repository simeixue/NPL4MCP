# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_and_decorate_tool_api_meta_exception
# lines: 128-134
def test_create_and_decorate_tool_api_meta_exception():
    # 覆盖 _create_and_decorate_tool 的异常分支
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools.ApiMetaClient.get_api_meta', side_effect=Exception('meta-fail')):
        mcp = DummyMCP()
        with pytest.raises(Exception) as e:
            api_tools._create_and_decorate_tool(mcp, 'ecs', 'DescribeInstances')
        assert 'meta-fail' in str(e.value)