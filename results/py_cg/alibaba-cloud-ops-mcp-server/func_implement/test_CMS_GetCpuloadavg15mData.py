# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_CMS_GetCpuloadavg15mData
# lines: 41-44
def test_CMS_GetCpuloadavg15mData():
    func = get_tool_func("CMS_GetCpuloadavg15mData")
    result = func(RegionId='cn-test', InstanceIds=['i-1'])
    assert isinstance(result, list)