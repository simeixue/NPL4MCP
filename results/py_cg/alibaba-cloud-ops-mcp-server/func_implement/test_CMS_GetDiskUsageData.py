# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_CMS_GetDiskUsageData
# lines: 59-62
def test_CMS_GetDiskUsageData():
    func = get_tool_func("CMS_GetDiskUsageData")
    result = func(RegionId='cn-test', InstanceIds=['i-1'])
    assert isinstance(result, list)