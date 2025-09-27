# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.get_tool_func
# lines: 5-6
def get_tool_func(name):
    return [f for f in oos_tools.tools if f.__name__ == name][0]