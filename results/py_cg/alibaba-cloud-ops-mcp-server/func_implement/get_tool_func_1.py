# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.get_tool_func
# lines: 6-7
def get_tool_func(name):
    return [f for f in cms_tools.tools if f.__name__ == name][0]