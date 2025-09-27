# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oss_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oss_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oss_tools.OSS_ListObjects
# lines: 60-77
def OSS_ListObjects(
    BucketName: str = Field(description='AlibabaCloud OSS Bucket Name'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
    Prefix: str = Field(description='AlibabaCloud OSS Bucket Name prefix', default=None)
):
    """获取指定OSS存储空间中的所有文件信息。"""
    if not BucketName:
        raise ValueError("Bucket name is required")
    client = create_client(region_id=RegionId)
    paginator = client.list_objects_v2_paginator()
    results = []
    for page in paginator.iter_page(oss.ListObjectsV2Request(
            bucket=BucketName,
            prefix=Prefix
        )):
        for object in page.contents:
            results.append(object.__str__())
    return results