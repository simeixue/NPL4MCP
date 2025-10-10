# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_chdb_tool.py
# module: tests.test_chdb_tool
# qname: tests.test_chdb_tool.TestChDBTools.test_run_chdb_select_query_simple
# lines: 16-21
    def test_run_chdb_select_query_simple(self):
        """Test running a simple SELECT query in chDB."""
        query = "SELECT 1 as test_value"
        result = run_chdb_select_query(query)
        self.assertIsInstance(result, list)
        self.assertIn("test_value", str(result))