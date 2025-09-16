# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/test/test_server.py
# module: test.test_server
# qname: test.test_server.TestCalculateExpression.test_equation_solving
# lines: 26-29
    def test_equation_solving(self):
        """测试方程求解"""
        self.assertEqual(calculate_expression("solve(x**2 - 4, x)"), "[-2.00000000000000, 2.00000000000000]")
        self.assertEqual(calculate_expression("solve([x + y - 1, x - y - 1], [x, y])"), "{x: 1, y: 0}")