# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_StartInstances
# lines: 76-91
def OOS_StartInstances(
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
):
    """批量启动ECS实例，适用于需要同时管理和启动多台ECS实例的场景，例如应用部署和高可用性场景。"""
    
    parameters = {
        'regionId': RegionId,
        'resourceType': 'ALIYUN::ECS::Instance',
        'targets': {
            'ResourceIds': InstanceIds,
            'RegionId': RegionId,
            'Type': 'ResourceIds'
        }
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-ECS-BulkyStartInstances', parameters=parameters)