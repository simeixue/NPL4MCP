# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_ReplaceSystemDisk
# lines: 67-70
def test_OOS_ReplaceSystemDisk():
    func = get_tool_func("OOS_ReplaceSystemDisk")
    result = func(RegionId='cn-test', InstanceIds=['i-1'], ImageId='img')
    assert hasattr(result, 'executions')