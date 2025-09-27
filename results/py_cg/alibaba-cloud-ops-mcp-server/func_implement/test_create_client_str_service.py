# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_client_str_service
# lines: 120-126
def test_create_client_str_service():
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools.OpenApiClient') as mock_client, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.create_config') as mock_cfg:
        mock_cfg.return_value = MagicMock()
        client = api_tools.create_client(service='ecs', region_id='cn-test')
        assert mock_client.called
        assert mock_cfg.return_value.endpoint == 'ecs.cn-test.aliyuncs.com'