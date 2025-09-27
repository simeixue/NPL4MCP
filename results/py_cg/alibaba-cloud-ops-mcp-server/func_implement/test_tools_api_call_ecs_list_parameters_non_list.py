# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_tools_api_call_ecs_list_parameters_non_list
# lines: 207-234
def test_tools_api_call_ecs_list_parameters_non_list():
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools.ApiMetaClient') as mock_ApiMetaClient, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.create_client') as mock_create_client, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.open_api_models') as mock_open_api_models, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.OpenApiUtilClient') as mock_OpenApiUtilClient, \
         patch('alibaba_cloud_ops_mcp_server.tools.api_tools.util_models') as mock_util_models:
        
        mock_ApiMetaClient.get_api_meta.return_value = fake_api_meta()
        mock_ApiMetaClient.get_service_version.return_value = '2023-01-01'
        mock_ApiMetaClient.get_service_style.return_value = 'RPC'
        mock_open_api_models.OpenApiRequest.return_value = MagicMock()
        mock_open_api_models.Params.return_value = MagicMock()
        mock_create_client.return_value.call_api.return_value = {'result': 'ok'}
        mock_OpenApiUtilClient.query.return_value = {}
        mock_util_models.RuntimeOptions.return_value = MagicMock()

        # 测试非列表类型的特殊参数
        params = {
            'InstanceIds': 'i-123',  # 字符串而不是列表
            'SecurityGroupIds': None,  # None值
            'RegionId': 'cn-hangzhou'
        }
        
        # 测试ECS服务
        result = api_tools._tools_api_call('ecs', 'DescribeInstances', params, None)
        # 验证传入query方法的参数
        query_args = mock_OpenApiUtilClient.query.call_args[0][0]
        assert query_args['InstanceIds'] == 'i-123'