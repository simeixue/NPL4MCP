# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.OOS_RunInstances
# lines: 137-156
def OOS_RunInstances(
    ImageId: str = Field(description='Image ID'),
    InstanceType: str = Field(description='Instance Type'),
    SecurityGroupId: str = Field(description='SecurityGroup ID'),
    VSwitchId: str = Field(description='VSwitch ID'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou'),
    Amount: int = Field(description='Number of ECS instances', default=1),
    InstanceName: str = Field(description='Instance Name', default='')
):
    """批量创建ECS实例，适用于需要同时创建多台ECS实例的场景，例如应用部署和高可用性场景。"""

    parameters = {
        'imageId': ImageId,
        'instanceType': InstanceType,
        'securityGroupId': SecurityGroupId,
        'vSwitchId': VSwitchId,
        'amount': Amount,
        'instanceName': InstanceName
    }
    return _start_execution_sync(region_id=RegionId, template_name='ACS-ECS-RunInstances', parameters=parameters)