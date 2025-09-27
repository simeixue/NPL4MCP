# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_CMS_GetCpuUsageData
# lines: 22-26
def test_CMS_GetCpuUsageData():
    func = get_tool_func("CMS_GetCpuUsageData")
    result = func(RegionId='cn-test', InstanceIds=['i-1'])
    assert isinstance(result, list)
    assert result[0]["value"] == 1