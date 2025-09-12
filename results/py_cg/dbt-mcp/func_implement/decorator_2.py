# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.mock_fastmcp.MockFastMCP.tool.decorator
# lines: 26-28
            def decorator(func):
                self.tools[func.__name__] = func
                return func