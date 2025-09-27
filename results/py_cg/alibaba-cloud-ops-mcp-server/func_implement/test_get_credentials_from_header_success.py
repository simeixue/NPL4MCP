# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_utils.py
# module: tests.alibabacloud.test_utils
# qname: tests.alibabacloud.test_utils.test_get_credentials_from_header_success
# lines: 17-34
def test_get_credentials_from_header_success():
    """测试从header成功获取凭证的情况"""
    with patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.get_http_request') as mock_get_request:
        mock_request = MagicMock()
        mock_request.headers = {
            'x-acs-accesskey-id': 'test_id',
            'x-acs-accesskey-secret': 'test_secret',
            'x-acs-security-token': 'test_token'
        }
        mock_get_request.return_value = mock_request
        
        result = utils.get_credentials_from_header()
        expected = {
            'AccessKeyId': 'test_id',
            'AccessKeySecret': 'test_secret',
            'SecurityToken': 'test_token'
        }
        assert result == expected