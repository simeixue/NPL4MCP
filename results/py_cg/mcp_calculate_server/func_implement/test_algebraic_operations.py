# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/test/test_server.py
# module: test.test_server
# qname: test.test_server.TestCalculateExpression.test_algebraic_operations
# lines: 14-18
    def test_algebraic_operations(self):
        """测试代数运算"""
        self.assertEqual(calculate_expression("expand((x + 1)**2)"), "x**2 + 2.0*x + 1.0")
        self.assertEqual(calculate_expression("factor(x**2 - 2*x - 15)"), "(x - 5.0)*(x + 3.0)")
        self.assertEqual(calculate_expression("simplify((x**2 - 1)/(x + 1))"), "x - 1.0")