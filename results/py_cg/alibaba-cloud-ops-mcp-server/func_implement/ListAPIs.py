# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/common_api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools.ListAPIs
# lines: 44-50
def ListAPIs(
        service: str = Field(description='AlibabaCloud service code')
):
    """
    Use PromptUnderstanding tool first to understand the user's query, Get the corresponding API list information through the service name to prepare for the subsequent selection of the appropriate API to call
    """
    return ApiMetaClient.get_apis_in_service(service)