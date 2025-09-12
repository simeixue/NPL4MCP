# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_show_command_limit_logic.mock_popen
# lines: 114-116
    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process