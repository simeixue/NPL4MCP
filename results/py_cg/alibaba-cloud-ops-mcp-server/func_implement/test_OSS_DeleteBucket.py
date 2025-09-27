# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_OSS_DeleteBucket
# lines: 51-54
def test_OSS_DeleteBucket():
    func = get_tool_func("OSS_DeleteBucket")
    result = func(RegionId='cn-test', BucketName='bucket')
    assert result == 'delete_bucket'