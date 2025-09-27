# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.DummyMCP.tool
# lines: 25-28
    def tool(self, name):
        def decorator(fn):
            return fn
        return decorator