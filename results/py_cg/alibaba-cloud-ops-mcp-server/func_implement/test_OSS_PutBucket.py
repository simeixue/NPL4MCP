# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.test_OSS_PutBucket
# lines: 45-48
def test_OSS_PutBucket():
    func = get_tool_func("OSS_PutBucket")
    result = func(RegionId='cn-test', BucketName='bucket')
    assert result == 'put_bucket'