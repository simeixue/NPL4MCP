# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_StopInstances
# lines: 43-46
def test_OOS_StopInstances():
    func = get_tool_func("OOS_StopInstances")
    result = func(RegionId='cn-test', InstanceIds=['i-1'], ForeceStop=True)
    assert hasattr(result, 'executions')