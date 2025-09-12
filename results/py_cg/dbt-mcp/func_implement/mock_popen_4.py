# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_list_command_timeout_handling.mock_popen
# lines: 231-232
    def mock_popen(*args, **kwargs):
        return MockProcessWithTimeout()