# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_full_refresh_flag_added_to_command.mock_popen
# lines: 258-260
    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process