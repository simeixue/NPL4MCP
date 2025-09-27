# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_RebootRDSInstances
# lines: 237-253
def OOS_RebootRDSInstances(
    InstanceIds: List[str] = Field(description='AlibabaCloud RDS instance ID List'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou')
):
    """批量重启RDS实例，适用于需要同时管理和重启多台RDS实例的场景。"""

    parameters = {
        'regionId': RegionId,
        'resourceType': 'ALIYUN::RDS::Instance',
        'targets': {
            'ResourceIds': InstanceIds,
            'RegionId': RegionId,
            'Type': 'ResourceIds'
        }
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-RDS-BulkyRestartInstances',
                                 parameters=parameters)