# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_CredentialsProvider_and_get_credentials
# lines: 58-69
def test_CredentialsProvider_and_get_credentials(mock_cred_client):
    # mock credentials client返回的credential对象
    cred = MagicMock()
    cred.access_key_id = 'id'
    cred.access_key_secret = 'secret'
    cred.security_token = 'token'
    mock_cred_client.return_value.get_credential.return_value = cred
    provider = oss_tools.CredentialsProvider()
    credentials = provider.get_credentials()
    assert credentials.access_key_id == 'id'
    assert credentials.access_key_secret == 'secret'
    assert credentials.security_token == 'token'