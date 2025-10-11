# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestHydrolixTools.test_list_databases
# lines: 44-49
    def test_list_databases(self):
        """Test listing databases."""
        result = list_databases.fn()
        # Parse JSON response
        databases = json.loads(result)
        self.assertIn(self.test_db, databases)