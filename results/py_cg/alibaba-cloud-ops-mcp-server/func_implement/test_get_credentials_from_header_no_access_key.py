# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_utils.py
# module: tests.alibabacloud.test_utils
# qname: tests.alibabacloud.test_utils.test_get_credentials_from_header_no_access_key
# lines: 36-44
def test_get_credentials_from_header_no_access_key():
    """测试header中没有access_key_id的情况"""
    with patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.get_http_request') as mock_get_request:
        mock_request = MagicMock()
        mock_request.headers = {}
        mock_get_request.return_value = mock_request
        
        result = utils.get_credentials_from_header()
        assert result is None