# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_OOS_RunInstances
# lines: 55-58
def test_OOS_RunInstances():
    func = get_tool_func("OOS_RunInstances")
    result = func(RegionId='cn-test', ImageId='img', InstanceType='ecs.t1', SecurityGroupId='sg', VSwitchId='vsw', Amount=1, InstanceName='test')
    assert hasattr(result, 'executions')