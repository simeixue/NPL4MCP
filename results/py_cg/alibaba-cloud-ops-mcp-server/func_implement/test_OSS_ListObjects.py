# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_OSS_ListObjects
# lines: 33-36
def test_OSS_ListObjects():
    func = get_tool_func("OSS_ListObjects")
    result = func(RegionId='cn-test', BucketName='bucket', Prefix='prefix')
    assert result == ['obj1']