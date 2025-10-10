# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_chdb_tool.py
# module: tests.test_chdb_tool
# qname: tests.test_chdb_tool.TestChDBTools.test_run_chdb_select_query_failure
# lines: 31-38
    def test_run_chdb_select_query_failure(self):
        """Test running a SELECT query with an error in chDB."""
        query = "SELECT * FROM non_existent_table_chDB"
        result = run_chdb_select_query(query)
        print(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["status"], "error")
        self.assertIn("message", result)