# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_StopRDSInstances
# lines: 79-82
def test_OOS_StopRDSInstances():
    func = get_tool_func("OOS_StopRDSInstances")
    result = func(RegionId='cn-test', InstanceIds=['rds-1'])
    assert hasattr(result, 'executions')