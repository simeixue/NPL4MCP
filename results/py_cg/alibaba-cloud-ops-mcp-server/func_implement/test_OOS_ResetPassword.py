# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_ResetPassword
# lines: 61-64
def test_OOS_ResetPassword():
    func = get_tool_func("OOS_ResetPassword")
    result = func(RegionId='cn-test', InstanceIds=['i-1'], Password='Abcd1234!')
    assert hasattr(result, 'executions')