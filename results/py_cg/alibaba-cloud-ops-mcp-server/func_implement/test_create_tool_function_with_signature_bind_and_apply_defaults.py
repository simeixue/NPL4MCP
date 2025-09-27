# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_tool_function_with_signature_bind_and_apply_defaults
# lines: 236-265
def test_create_tool_function_with_signature_bind_and_apply_defaults():
    """测试func_code函数中的signature.bind和apply_defaults调用"""
    api_meta = {
        'parameters': [
            {'name': 'param1', 'schema': {'type': 'string', 'required': False}},
            {'name': 'param2', 'schema': {'type': 'integer', 'required': True}}
        ],
        'summary': 'Test function'
    }
    
    schemas = api_tools._create_function_schemas('test', 'TestApi', api_meta)
    fields = schemas['TestApi']
    
    # 创建函数
    func = api_tools._create_tool_function_with_signature('test', 'TestApi', fields, 'Test function')
    
    # 测试函数调用，确保执行到signature.bind和apply_defaults
    with patch('alibaba_cloud_ops_mcp_server.tools.api_tools._tools_api_call') as mock_call:
        mock_call.return_value = {'result': 'success'}
        
        # 调用函数，传入部分参数，让apply_defaults生效
        result = func(param2=123)  # 只传入required参数，让param1使用默认值
        
        # 验证_tools_api_call被调用
        mock_call.assert_called_once()
        call_args = mock_call.call_args[1]['parameters']
        
        # 验证参数绑定和默认值应用
        assert 'param1' in call_args  # 默认值被应用
        assert call_args['param2'] == 123  # 传入的参数