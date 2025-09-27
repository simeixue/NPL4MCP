# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_RebootInstances
# lines: 116-133
def OOS_RebootInstances(
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
    ForeceStop: bool = Field(description='Is forced shutdown required', default=False)
):
    """批量重启ECS实例，适用于需要同时管理和重启多台ECS实例的场景。"""
    
    parameters = {
        'regionId': RegionId,
        'resourceType': 'ALIYUN::ECS::Instance',
        'targets': {
            'ResourceIds': InstanceIds,
            'RegionId': RegionId,
            'Type': 'ResourceIds'
        },
        'forceStop': ForeceStop
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-ECS-BulkyRebootInstances', parameters=parameters)