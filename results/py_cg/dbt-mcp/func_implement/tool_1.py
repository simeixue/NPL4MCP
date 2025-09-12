# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.mock_fastmcp.MockFastMCP.tool
# lines: 25-30
        def tool(self, **kwargs):
            def decorator(func):
                self.tools[func.__name__] = func
                return func

            return decorator