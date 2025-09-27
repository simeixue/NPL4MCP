# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_CMS_GetDiskUsedData
# lines: 71-74
def test_CMS_GetDiskUsedData():
    func = get_tool_func("CMS_GetDiskUsedData")
    result = func(RegionId='cn-test', InstanceIds=['i-1'])
    assert isinstance(result, list)