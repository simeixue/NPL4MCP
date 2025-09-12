# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_run_command_adds_quiet_flag_to_verbose_commands.mock_popen
# lines: 140-142
    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process