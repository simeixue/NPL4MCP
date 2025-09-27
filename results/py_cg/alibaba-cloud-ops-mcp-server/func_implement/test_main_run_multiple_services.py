# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_main_run_multiple_services
# lines: 70-88
def test_main_run_multiple_services(mock_create_api_tools, mock_FastMCP):
    """测试指定多个services的情况"""
    with patch('alibaba_cloud_ops_mcp_server.server.oss_tools.tools', [lambda: None]), \
         patch('alibaba_cloud_ops_mcp_server.server.oos_tools.tools', [lambda: None]), \
         patch('alibaba_cloud_ops_mcp_server.server.cms_tools.tools', [lambda: None]), \
         patch('alibaba_cloud_ops_mcp_server.server.common_api_tools.tools', [lambda: None, lambda: None]):
        from alibaba_cloud_ops_mcp_server import server
        mcp = MagicMock()
        mock_FastMCP.return_value = mcp
        # 调用main函数，指定多个services
        server.main.callback(transport='sse', port=9000, host='0.0.0.0', services='ecs,vpc,rds',
                             headers_credential_only=None, env='domestic')
        mock_FastMCP.assert_called_once_with(
            name='alibaba-cloud-ops-mcp-server',
            port=9000, host='0.0.0.0', stateless_http=True)
        # common_api_tools 2 + oss/oos/cms 各1 = 5
        assert mcp.tool.call_count == 5
        mock_create_api_tools.assert_called_once()
        mcp.run.assert_called_once_with(transport='sse')