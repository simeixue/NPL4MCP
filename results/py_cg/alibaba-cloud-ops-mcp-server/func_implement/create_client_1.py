# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools.create_client
# lines: 19-22
def create_client(region_id: str) -> oos20190601Client:
    config = create_config()
    config.endpoint = f'oos.{region_id}.aliyuncs.com'
    return oos20190601Client(config)