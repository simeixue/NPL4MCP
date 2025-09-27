# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oss_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oss_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oss_tools.OSS_PutBucket
# lines: 81-105
def OSS_PutBucket(
    BucketName: str = Field(description='AlibabaCloud OSS Bucket Name'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
    StorageClass: str = Field(description='The Storage Type of AlibabaCloud OSS Bucket, The value range is as follows: '
                                          'Standard (default): standard storage, '
                                          'IA: infrequent access, Archive: archive storage, '
                                          'ColdArchive: cold archive storage, '
                                          'DeepColdArchive: deep cold archive storage', default='Standard'),
    DataRedundancyType: str = Field(description='The data disaster recovery type of AlibabaCloud OSS Bucket, '
                                                'LRS (default): Locally redundant LRS, which stores your data '
                                                'redundantly on different storage devices in the same availability zone. '
                                                'ZRS: Intra-city redundant ZRS, which uses a multi-availability zone '
                                                '(AZ) mechanism to store your data redundantly in three availability '
                                                'zones in the same region.', default='LRS')
):
    """创建一个新的OSS存储空间。"""
    client = create_client(region_id=RegionId)
    result = client.put_bucket(oss.PutBucketRequest(
        bucket=BucketName,
        create_bucket_configuration=oss.CreateBucketConfiguration(
            storage_class=StorageClass,
            data_redundancy_type=DataRedundancyType
        )
    ))
    return result.__str__()