# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_OSS_ListBuckets
# lines: 27-30
def test_OSS_ListBuckets():
    func = get_tool_func("OSS_ListBuckets")
    result = func(RegionId='cn-test', Prefix='prefix')
    assert result == ['bucket1']