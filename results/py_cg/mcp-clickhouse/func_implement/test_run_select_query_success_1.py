# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestClickhouseTools.test_run_select_query_success
# lines: 65-72
    def test_run_select_query_success(self):
        """Test running a SELECT query successfully."""
        query = f"SELECT * FROM {self.test_db}.{self.test_table}"
        result = run_select_query(query)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result["rows"]), 2)
        self.assertEqual(result["rows"][0][0], 1)
        self.assertEqual(result["rows"][0][1], "Alice")