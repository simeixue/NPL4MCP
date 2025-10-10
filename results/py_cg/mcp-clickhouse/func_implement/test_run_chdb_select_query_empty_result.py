# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_chdb_tool.py
# module: tests.test_chdb_tool
# qname: tests.test_chdb_tool.TestChDBTools.test_run_chdb_select_query_empty_result
# lines: 40-46
    def test_run_chdb_select_query_empty_result(self):
        """Test running a SELECT query that returns empty result in chDB."""
        query = "SELECT 1 WHERE 1 = 0"
        result = run_chdb_select_query(query)
        print(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)