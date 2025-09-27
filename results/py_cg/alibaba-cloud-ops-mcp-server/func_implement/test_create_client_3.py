# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_create_client
# lines: 164-191
def test_create_client():
    """测试create_client函数的基本功能"""
    with patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.create_config') as mock_create_config, \
         patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.oos20190601Client') as mock_client:
        
        # 模拟配置对象
        mock_config = MagicMock()
        mock_create_config.return_value = mock_config
        
        # 模拟客户端对象
        mock_client_instance = MagicMock()
        mock_client.return_value = mock_client_instance
        
        # 调用函数
        region_id = 'cn-hangzhou'
        result = oos_tools.create_client(region_id)
        
        # 验证create_config被调用
        mock_create_config.assert_called_once()
        
        # 验证endpoint被正确设置
        assert mock_config.endpoint == f'oos.{region_id}.aliyuncs.com'
        
        # 验证oos20190601Client被正确调用
        mock_client.assert_called_once_with(mock_config)
        
        # 验证返回的是客户端实例
        assert result == mock_client_instance