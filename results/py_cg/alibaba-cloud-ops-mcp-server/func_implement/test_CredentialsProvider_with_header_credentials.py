# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_CredentialsProvider_with_header_credentials
# lines: 72-83
def test_CredentialsProvider_with_header_credentials(mock_get_creds):
    """测试从header获取凭证的CredentialsProvider"""
    mock_get_creds.return_value = {
        'AccessKeyId': 'header_id',
        'AccessKeySecret': 'header_secret',
        'SecurityToken': 'header_token'
    }
    provider = oss_tools.CredentialsProvider()
    credentials = provider.get_credentials()
    assert credentials.access_key_id == 'header_id'
    assert credentials.access_key_secret == 'header_secret'
    assert credentials.security_token == 'header_token'