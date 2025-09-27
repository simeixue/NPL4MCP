# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_create_client_different_regions
# lines: 194-221
def test_create_client_different_regions():
    """测试create_client函数在不同region下的行为"""
    with patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.create_config') as mock_create_config, \
         patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.oos20190601Client') as mock_client:
        
        mock_config = MagicMock()
        mock_create_config.return_value = mock_config
        mock_client_instance = MagicMock()
        mock_client.return_value = mock_client_instance
        
        # 测试不同的region
        test_regions = ['cn-hangzhou', 'cn-beijing', 'us-west-1']
        
        for region_id in test_regions:
            # 重置mock
            mock_config.reset_mock()
            mock_client.reset_mock()
            
            # 调用函数
            result = oos_tools.create_client(region_id)
            
            # 验证endpoint格式正确
            expected_endpoint = f'oos.{region_id}.aliyuncs.com'
            assert mock_config.endpoint == expected_endpoint
            
            # 验证客户端被创建
            mock_client.assert_called_once_with(mock_config)
            assert result == mock_client_instance