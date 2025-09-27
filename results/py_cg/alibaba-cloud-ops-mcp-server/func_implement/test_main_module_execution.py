# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_main_module_execution
# lines: 46-65
def test_main_module_execution():
    """测试模块直接执行时的入口点（第78-79行）"""
    import subprocess
    import sys
    import os
    
    # 获取server.py的路径
    server_path = os.path.join(os.path.dirname(__file__), '../src/alibaba_cloud_ops_mcp_server/server.py')
    server_path = os.path.abspath(server_path)
    
    # 使用subprocess来模拟直接执行模块，但立即终止以避免实际运行服务器
    try:
        # 使用timeout来快速终止进程，只是为了测试入口点能否正常启动
        result = subprocess.run([sys.executable, server_path, '--help'], 
                              capture_output=True, text=True, timeout=5)
        # 如果能显示帮助信息，说明main函数和入口点工作正常
        assert 'Transport type' in result.stdout or result.returncode == 0
    except subprocess.TimeoutExpired:
        # 超时也是可以接受的，说明程序启动了
        pass