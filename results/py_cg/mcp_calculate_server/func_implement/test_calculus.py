# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/test/test_server.py
# module: test.test_server
# qname: test.test_server.TestCalculateExpression.test_calculus
# lines: 20-24
    def test_calculus(self):
        """测试微积分"""
        self.assertEqual(calculate_expression("diff(sin(x), x)"), "cos(x)")
        self.assertEqual(calculate_expression("integrate(exp(x), x)"), "exp(x)")
        self.assertEqual(calculate_expression("limit(tan(x)/x, x, 0)"), "1.00000000000000")