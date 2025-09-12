# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.mock_fastmcp.MockFastMCP.tool.decorator
# lines: 40-42
            def decorator(func):
                self.tools[func.__name__] = func
                return func