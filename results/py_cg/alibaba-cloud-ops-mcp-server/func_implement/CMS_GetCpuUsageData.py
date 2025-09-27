# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/cms_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.cms_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.cms_tools.CMS_GetCpuUsageData
# lines: 43-48
def CMS_GetCpuUsageData(
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou')
):
    """获取ECS实例的CPU使用率数据"""
    return _get_cms_metric_data(RegionId, InstanceIds, 'cpu_total')