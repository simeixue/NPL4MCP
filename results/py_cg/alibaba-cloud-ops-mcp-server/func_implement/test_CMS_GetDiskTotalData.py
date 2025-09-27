# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_CMS_GetDiskTotalData
# lines: 65-68
def test_CMS_GetDiskTotalData():
    func = get_tool_func("CMS_GetDiskTotalData")
    result = func(RegionId='cn-test', InstanceIds=['i-1'])
    assert isinstance(result, list)