# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/test/test_server.py
# module: test.test_server
# qname: test.test_server.TestCalculateExpression.test_basic_operations
# lines: 8-12
    def test_basic_operations(self):
        """测试基础运算"""
        self.assertEqual(calculate_expression("2 + 3*5"), "17")
        self.assertEqual(calculate_expression("10 / 2"), "5.0")
        self.assertEqual(calculate_expression("2**8"), "256")