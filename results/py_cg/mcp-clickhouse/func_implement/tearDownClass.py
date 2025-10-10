# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_tool.py
# module: tests.test_tool
# qname: tests.test_tool.TestClickhouseTools.tearDownClass
# lines: 40-42
    def tearDownClass(cls):
        """Clean up the environment after tests."""
        cls.client.command(f"DROP DATABASE IF EXISTS {cls.test_db}")