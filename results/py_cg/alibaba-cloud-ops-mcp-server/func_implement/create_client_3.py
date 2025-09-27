# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oss_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oss_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oss_tools.create_client
# lines: 35-41
def create_client(region_id: str) -> oss.Client:
    credentials_provider = CredentialsProvider()
    cfg = oss.config.load_default()
    cfg.user_agent = 'alibaba-cloud-ops-mcp-server'
    cfg.credentials_provider = credentials_provider
    cfg.region = region_id
    return oss.Client(cfg)