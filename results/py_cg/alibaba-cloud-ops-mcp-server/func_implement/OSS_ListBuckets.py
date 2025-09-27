# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oss_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oss_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oss_tools.OSS_ListBuckets
# lines: 45-56
def OSS_ListBuckets(
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
    Prefix: str = Field(description='AlibabaCloud OSS Bucket Name prefix', default=None)
):
    """列出指定区域的所有OSS存储空间。"""
    client = create_client(region_id=RegionId)
    paginator = client.list_buckets_paginator()
    results = []
    for page in paginator.iter_page(oss.ListBucketsRequest(prefix=Prefix)):
        for bucket in page.buckets:
            results.append(bucket.__str__())
    return results