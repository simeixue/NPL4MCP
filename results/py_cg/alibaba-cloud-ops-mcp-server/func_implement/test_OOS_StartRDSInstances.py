# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_StartRDSInstances
# lines: 73-76
def test_OOS_StartRDSInstances():
    func = get_tool_func("OOS_StartRDSInstances")
    result = func(RegionId='cn-test', InstanceIds=['rds-1'])
    assert hasattr(result, 'executions')