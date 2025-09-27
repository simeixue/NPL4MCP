# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.get_tool_func
# lines: 5-6
def get_tool_func(name):
    return [f for f in oss_tools.tools if f.__name__ == name][0]