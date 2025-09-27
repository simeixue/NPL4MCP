# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_OSS_ListObjects_no_bucket
# lines: 39-42
def test_OSS_ListObjects_no_bucket():
    func = get_tool_func("OSS_ListObjects")
    with pytest.raises(ValueError):
        func(RegionId='cn-test', BucketName='', Prefix='prefix')