# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestClickhouseTools.test_run_select_query_failure
# lines: 74-82
    def test_run_select_query_failure(self):
        """Test running a SELECT query with an error."""
        query = f"SELECT * FROM {self.test_db}.non_existent_table"

        # Should raise ToolError
        with self.assertRaises(ToolError) as context:
            run_select_query(query)

        self.assertIn("Query execution failed", str(context.exception))