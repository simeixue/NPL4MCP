# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestHydrolixTools.test_list_tables_without_like
# lines: 51-56
    def test_list_tables_without_like(self):
        """Test listing tables without a 'LIKE' filter."""
        result = list_tables.fn(self.test_db)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], self.test_table)