# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_chdb_tool.py
# module: tests.test_chdb_tool
# qname: tests.test_chdb_tool.TestChDBTools.test_run_chdb_select_query_with_url_table_function
# lines: 23-29
    def test_run_chdb_select_query_with_url_table_function(self):
        """Test running a SELECT query with url table function in chDB."""
        query = "SELECT COUNT(1) FROM url('https://datasets.clickhouse.com/hits_compatible/athena_partitioned/hits_0.parquet', 'Parquet')"
        result = run_chdb_select_query(query)
        print(result)
        self.assertIsInstance(result, list)
        self.assertIn("1000000", str(result))