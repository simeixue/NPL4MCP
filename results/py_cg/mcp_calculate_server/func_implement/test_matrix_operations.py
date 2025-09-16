# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/test/test_server.py
# module: test.test_server
# qname: test.test_server.TestCalculateExpression.test_matrix_operations
# lines: 31-35
    def test_matrix_operations(self):
        """测试矩阵运算"""
        self.assertEqual(calculate_expression("Matrix([[1, 2], [3, 4]]).inv()"), 
                         "Matrix([[-2.00000000000000, 1.00000000000000], [1.50000000000000, -0.500000000000000]])")
        self.assertEqual(calculate_expression("Matrix([[1, 2], [3, 4]]).det()"), "-2.00000000000000")