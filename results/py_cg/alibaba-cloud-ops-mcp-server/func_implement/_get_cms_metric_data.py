# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/cms_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.cms_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.cms_tools._get_cms_metric_data
# lines: 26-40
def _get_cms_metric_data(region_id: str, instance_ids: List[str], metric_name: str):
    client = create_client(region_id)
    dimesion = []
    for instance_id in instance_ids:
        dimesion.append({
            'instanceId': instance_id
        })
    describe_metric_last_request = cms_20190101_models.DescribeMetricLastRequest(
        namespace='acs_ecs_dashboard',
        metric_name=metric_name,
        dimensions=json.dumps(dimesion),
    )
    describe_metric_last_resp = client.describe_metric_last(describe_metric_last_request)
    logger.info(f'CMS Tools response: {describe_metric_last_resp.body}')
    return describe_metric_last_resp.body.datapoints