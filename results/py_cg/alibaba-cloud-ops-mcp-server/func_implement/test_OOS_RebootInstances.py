# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_RebootInstances
# lines: 49-52
def test_OOS_RebootInstances():
    func = get_tool_func("OOS_RebootInstances")
    result = func(RegionId='cn-test', InstanceIds=['i-1'], ForeceStop=True)
    assert hasattr(result, 'executions')