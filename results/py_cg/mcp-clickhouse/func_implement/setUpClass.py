# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_chdb_tool.py
# module: tests.test_chdb_tool
# qname: tests.test_chdb_tool.TestChDBTools.setUpClass
# lines: 12-14
    def setUpClass(cls):
        """Set up the environment before chDB tests."""
        cls.client = create_chdb_client()