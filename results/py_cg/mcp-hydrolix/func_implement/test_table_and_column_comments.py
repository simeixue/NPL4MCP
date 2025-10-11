# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestHydrolixTools.test_table_and_column_comments
# lines: 84-99
    def test_table_and_column_comments(self):
        """Test that table and column comments are correctly retrieved."""
        result = list_tables.fn(self.test_db)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

        table_info = result[0]
        # Verify table comment
        self.assertEqual(table_info["comment"], "Test table for unit testing")

        # Get columns by name for easier testing
        columns = {col["name"]: col for col in table_info["columns"]}

        # Verify column comments
        self.assertEqual(columns["id"]["comment"], "Primary identifier")
        self.assertEqual(columns["name"]["comment"], "User name field")