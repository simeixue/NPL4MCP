# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/test/test_server.py
# module: test.test_server
# qname: test.test_server.TestCalculateExpression.test_error_handling
# lines: 37-40
    def test_error_handling(self):
        """测试错误处理"""
        self.assertTrue(calculate_expression("1 / 0").startswith("Error:"))
        self.assertTrue(calculate_expression("invalid expression").startswith("Error:"))