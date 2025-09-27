# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/cms_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.cms_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.cms_tools.create_client
# lines: 20-23
def create_client(region_id: str) -> cms20190101Client:
    config = create_config()
    config.endpoint = f'metrics.{region_id}.aliyuncs.com'
    return cms20190101Client(config)