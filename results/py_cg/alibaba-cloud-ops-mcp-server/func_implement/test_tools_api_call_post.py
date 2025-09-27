# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_tools_api_call_post
# lines: 67-83
def test_tools_api_call_post():
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools.ApiMetaClient') as mock_ApiMetaClient, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.create_client') as mock_create_client, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.open_api_models') as mock_open_api_models, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.OpenApiUtilClient') as mock_OpenApiUtilClient, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.util_models') as mock_util_models:
        mock_ApiMetaClient.get_api_meta.return_value = fake_api_meta(post=True)
        mock_ApiMetaClient.get_service_version.return_value = '2023-01-01'
        mock_ApiMetaClient.get_service_style.return_value = 'RPC'
        mock_open_api_models.OpenApiRequest.return_value = MagicMock()
        mock_open_api_models.Params.return_value = MagicMock()
        mock_create_client.return_value.call_api.return_value = {'result': 'ok'}
        mock_OpenApiUtilClient.query.return_value = {}
        mock_util_models.RuntimeOptions.return_value = MagicMock()
        params = {'InstanceId': 'i-123', 'RegionId': 'cn-hangzhou'}
        result = api_tools._tools_api_call('ecs', 'DescribeInstances', params, None)
        assert result == {'result': 'ok'}