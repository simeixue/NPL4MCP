# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.mock_process
# lines: 11-16
def mock_process():
    class MockProcess:
        def communicate(self, timeout=None):
            return "command output", None

    return MockProcess()