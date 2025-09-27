# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_main_run_with_logging
# lines: 94-106
def test_main_run_with_logging(mock_logger, mock_create_api_tools, mock_FastMCP):
    """测试日志输出（第77行）"""
    with patch('alibaba_cloud_ops_mcp_server.server.oss_tools.tools', []), \
         patch('alibaba_cloud_ops_mcp_server.server.oos_tools.tools', []), \
         patch('alibaba_cloud_ops_mcp_server.server.cms_tools.tools', []):
        from alibaba_cloud_ops_mcp_server import server
        mcp = MagicMock()
        mock_FastMCP.return_value = mcp
        # 调用main函数
        server.main.callback(transport='streamable-http', port=8080, host='localhost', services=None,
                             headers_credential_only=None, env='domestic')
        # 验证日志被调用
        mock_logger.debug.assert_called_once_with('mcp server is running on streamable-http mode.')