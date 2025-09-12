# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_cli_integration.py
# module: tests.unit.dbt_cli.test_cli_integration
# qname: tests.unit.dbt_cli.test_cli_integration.TestDbtCliIntegration.test_dbt_command_execution.mock_tool_decorator.decorator
# lines: 29-31
            def decorator(func):
                tools[func.__name__] = func
                return func