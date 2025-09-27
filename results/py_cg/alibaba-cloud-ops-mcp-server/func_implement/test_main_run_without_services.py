# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_main_run_without_services
# lines: 26-43
def test_main_run_without_services(mock_create_api_tools, mock_FastMCP):
    """测试不指定services参数时的情况"""
    with patch('alibaba_cloud_ops_mcp_server.server.oss_tools.tools', [lambda: None]), \
         patch('alibaba_cloud_ops_mcp_server.server.oos_tools.tools', [lambda: None]), \
         patch('alibaba_cloud_ops_mcp_server.server.cms_tools.tools', [lambda: None]):
        from alibaba_cloud_ops_mcp_server import server
        mcp = MagicMock()
        mock_FastMCP.return_value = mcp
        # 调用main函数，不指定services
        server.main.callback(transport='stdio', port=8000, host='127.0.0.1', services=None,
                             headers_credential_only=None, env='domestic')
        mock_FastMCP.assert_called_once_with(
            name='alibaba-cloud-ops-mcp-server',
            port=8000, host='127.0.0.1', stateless_http=True)
        # 不指定services时，应该只有oss/oos/cms的工具被添加，没有common_api_tools
        assert mcp.tool.call_count == 3  # oss/oos/cms 各1
        mock_create_api_tools.assert_called_once()
        mcp.run.assert_called_once_with(transport='stdio')