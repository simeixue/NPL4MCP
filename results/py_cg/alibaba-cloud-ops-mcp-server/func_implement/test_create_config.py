# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_utils.py
# module: tests.alibabacloud.test_utils
# qname: tests.alibabacloud.test_utils.test_create_config
# lines: 4-15
def test_create_config():
    with patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.CredClient') as mock_cred, \
         patch('alibaba_cloud_ops_mcp_server.alibabacloud.utils.Config') as mock_cfg:
        cred = MagicMock()
        mock_cred.return_value = cred
        cfg = MagicMock()
        mock_cfg.return_value = cfg
        result = utils.create_config()
        assert result is cfg
        assert cfg.user_agent == 'alibaba-cloud-ops-mcp-server'
        mock_cred.assert_called_once()
        mock_cfg.assert_called_once_with(credential=cred)