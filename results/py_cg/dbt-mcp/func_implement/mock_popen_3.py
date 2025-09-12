# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_show_command_correctly_formatted.mock_popen
# lines: 200-202
    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process