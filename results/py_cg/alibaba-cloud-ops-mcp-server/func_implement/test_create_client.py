# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_create_client
# lines: 87-98
def test_create_client(mock_oss, mock_provider):
    # mock config和Client
    mock_cfg = MagicMock()
    mock_oss.config.load_default.return_value = mock_cfg
    mock_client = MagicMock()
    mock_oss.Client.return_value = mock_client
    mock_provider.return_value = MagicMock()
    client = oss_tools.create_client('cn-test')
    assert client is mock_client
    assert mock_cfg.user_agent == 'alibaba-cloud-ops-mcp-server'
    assert mock_cfg.region == 'cn-test'
    assert mock_cfg.credentials_provider == mock_provider.return_value 