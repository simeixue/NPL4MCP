# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_vars_not_added_when_none.mock_popen
# lines: 302-304
    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process