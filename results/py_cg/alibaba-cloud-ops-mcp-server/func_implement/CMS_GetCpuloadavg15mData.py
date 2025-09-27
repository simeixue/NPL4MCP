# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/cms_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.cms_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.cms_tools.CMS_GetCpuloadavg15mData
# lines: 70-75
def CMS_GetCpuloadavg15mData(
    InstanceIds: List[str] = Field(description='AlibabaCloud ECS instance ID List'),
    RegionId: str = Field(description='AlibabaCloud region ID', default='cn-hangzhou')
):
    """获取CPU十五分钟平均负载指标数据"""
    return _get_cms_metric_data(RegionId, InstanceIds, 'load_15m')