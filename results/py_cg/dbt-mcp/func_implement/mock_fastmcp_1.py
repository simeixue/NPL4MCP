# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.mock_fastmcp
# lines: 20-33
def mock_fastmcp():
    class MockFastMCP:
        def __init__(self):
            self.tools = {}

        def tool(self, **kwargs):
            def decorator(func):
                self.tools[func.__name__] = func
                return func

            return decorator

    fastmcp = MockFastMCP()
    return fastmcp, fastmcp.tools