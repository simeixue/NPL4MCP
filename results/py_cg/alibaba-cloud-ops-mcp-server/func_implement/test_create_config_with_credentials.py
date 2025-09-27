# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_utils.py
# module: tests.alibabacloud.test_utils
# qname: tests.alibabacloud.test_utils.test_create_config_with_credentials
# lines: 56-75
def test_create_config_with_credentials():
    """测试使用header中的凭证创建config的情况"""
    with patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.get_credentials_from_header') as mock_get_creds, \
         patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.Config') as mock_cfg:
        mock_get_creds.return_value = {
            'AccessKeyId': 'test_id',
            'AccessKeySecret': 'test_secret',
            'SecurityToken': 'test_token'
        }
        cfg = MagicMock()
        mock_cfg.return_value = cfg
        
        result = utils.create_config()
        assert result is cfg
        assert cfg.user_agent == 'alibaba-cloud-ops-mcp-server'
        mock_cfg.assert_called_once_with(
            access_key_id='test_id',
            access_key_secret='test_secret',
            security_token='test_token'
        ) 