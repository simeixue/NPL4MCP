# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools.create_api_tools
# lines: 267-270
def create_api_tools(mcp: FastMCP, config:dict):
    for service_code, apis in config.items():
        for api_name in apis:
            _create_and_decorate_tool(mcp, service_code, api_name)