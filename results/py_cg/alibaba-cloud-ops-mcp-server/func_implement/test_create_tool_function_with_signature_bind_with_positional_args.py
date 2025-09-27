# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_tool_function_with_signature_bind_with_positional_args
# lines: 298-327
def test_create_tool_function_with_signature_bind_with_positional_args():
    """测试func_code函数中使用位置参数的情况"""
    api_meta = {
        'parameters': [
            {'name': 'param1', 'schema': {'type': 'string', 'required': False}},
            {'name': 'param2', 'schema': {'type': 'integer', 'required': False}}
        ],
        'summary': 'Test function'
    }
    
    schemas = api_tools._create_function_schemas('test', 'TestApi', api_meta)
    fields = schemas['TestApi']
    
    # 创建函数
    func = api_tools._create_tool_function_with_signature('test', 'TestApi', fields, 'Test function')
    
    # 测试使用位置参数
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools._tools_api_call') as mock_call:
        mock_call.return_value = {'result': 'success'}
        
        # 使用位置参数调用
        result = func('value1', 789)
        
        # 验证_tools_api_call被调用
        mock_call.assert_called_once()
        call_args = mock_call.call_args[1]['parameters']
        
        # 验证位置参数被正确绑定
        assert call_args['param1'] == 'value1'
        assert call_args['param2'] == 789