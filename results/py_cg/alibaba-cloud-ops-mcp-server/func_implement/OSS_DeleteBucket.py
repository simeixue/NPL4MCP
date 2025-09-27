# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oss_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oss_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oss_tools.OSS_DeleteBucket
# lines: 109-116
def OSS_DeleteBucket(
    BucketName: str = Field(description='AlibabaCloud OSS Bucket Name'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou')
):
    """删除指定的OSS存储空间。"""
    client = create_client(region_id=RegionId)
    result = client.delete_bucket(oss.DeleteBucketRequest(bucket=BucketName))
    return result.__str__()