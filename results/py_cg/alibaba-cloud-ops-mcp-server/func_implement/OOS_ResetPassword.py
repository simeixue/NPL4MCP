# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_ResetPassword
# lines: 160-176
def OOS_ResetPassword(
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    Password: str = Field(description='The password of the ECS instance must be 8-30 characters and must contain only the following characters: lowercase letters, uppercase letters, numbers, and special characters only.（）~！@#$%^&*-_+=（40：<>，？/'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
):
    """批量修改ECS实例的密码，请注意，本操作将会重启ECS实例"""
    parameters = {
        'regionId': RegionId,
        'resourceType': 'ALIYUN::ECS::Instance',
        'targets': {
            'ResourceIds': InstanceIds,
            'RegionId': RegionId,
            'Type': 'ResourceIds'
        },
        'password': Password
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-ECS-BulkyResetPassword', parameters=parameters)