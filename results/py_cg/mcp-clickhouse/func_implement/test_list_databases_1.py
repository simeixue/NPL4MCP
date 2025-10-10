# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestClickhouseTools.test_list_databases
# lines: 44-49
    def test_list_databases(self):
        """Test listing databases."""
        result = list_databases()
        # Parse JSON response
        databases = json.loads(result)
        self.assertIn(self.test_db, databases)