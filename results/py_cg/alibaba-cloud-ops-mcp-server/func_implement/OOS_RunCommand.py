# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_RunCommand
# lines: 49-72
def OOS_RunCommand(
    Command: str = Field(description='Content of the command executed on the ECS instance'),
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
    CommandType: str = Field(description='The type of command executed on the ECS instance, optional value：RunShellScript，RunPythonScript，RunPerlScript，RunBatScript，RunPowerShellScript', default='RunShellScript')
):
    """批量在多台ECS实例上运行云助手命令，适用于需要同时管理多台ECS实例的场景，如应用程序管理和资源标记操作等。"""
    
    parameters = {
        'regionId': RegionId,
        'resourceType': 'ALIYUN::ECS::Instance',
        'targets': {
            'ResourceIds': InstanceIds,
            'RegionId': RegionId,
            'Type': 'ResourceIds',
            'Parameters': {
                'RegionId': RegionId,
                'Status': 'Running'
            }
        },
        "commandType": CommandType,
        "commandContent": Command
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-ECS-BulkyRunCommand', parameters=parameters)