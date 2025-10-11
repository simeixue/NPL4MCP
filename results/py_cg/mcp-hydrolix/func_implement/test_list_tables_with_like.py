# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestHydrolixTools.test_list_tables_with_like
# lines: 58-63
    def test_list_tables_with_like(self):
        """Test listing tables with a 'LIKE' filter."""
        result = list_tables.fn(self.test_db, like=f"{self.test_table}%")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], self.test_table)