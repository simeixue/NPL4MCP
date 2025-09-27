# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_RebootRDSInstances
# lines: 85-88
def test_OOS_RebootRDSInstances():
    func = get_tool_func("OOS_RebootRDSInstances")
    result = func(RegionId='cn-test', InstanceIds=['rds-1'])
    assert hasattr(result, 'executions')