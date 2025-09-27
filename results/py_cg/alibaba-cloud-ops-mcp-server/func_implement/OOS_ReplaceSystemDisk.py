# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_ReplaceSystemDisk
# lines: 179-195
def OOS_ReplaceSystemDisk(
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    ImageId: str = Field(description='Image ID'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou')
):
    """批量替换ECS实例的系统盘，更换操作系统"""
    parameters = {
        'regionId': RegionId,
        'resourceType': 'ALIYUN::ECS::Instance',
        'targets': {
            'ResourceIds': InstanceIds,
            'RegionId': RegionId,
            'Type': 'ResourceIds'
        },
        'imageId': ImageId
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-ECS-BulkyReplaceSystemDisk', parameters=parameters)