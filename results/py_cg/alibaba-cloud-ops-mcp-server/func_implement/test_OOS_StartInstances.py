# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_StartInstances
# lines: 37-40
def test_OOS_StartInstances():
    func = get_tool_func("OOS_StartInstances")
    result = func(RegionId='cn-test', InstanceIds=['i-1'])
    assert hasattr(result, 'executions')