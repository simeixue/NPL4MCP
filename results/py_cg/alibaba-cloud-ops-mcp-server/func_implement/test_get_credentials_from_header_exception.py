# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_utils.py
# module: tests.alibabacloud.test_utils
# qname: tests.alibabacloud.test_utils.test_get_credentials_from_header_exception
# lines: 46-54
def test_get_credentials_from_header_exception():
    """测试get_http_request抛出异常的情况"""
    with patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.get_http_request') as mock_get_request, \
         patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.logger') as mock_logger:
        mock_get_request.side_effect = Exception('test error')
        
        result = utils.get_credentials_from_header()
        assert result is None
        mock_logger.info.assert_called_once_with('get_credentials_from_header error: test error')