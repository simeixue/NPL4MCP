# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_RunCommand
# lines: 31-34
def test_OOS_RunCommand():
    func = get_tool_func("OOS_RunCommand")
    result = func(RegionId='cn-test', InstanceIds=['i-1'], CommandType='RunShellScript', Command='echo hello')
    assert hasattr(result, 'executions')