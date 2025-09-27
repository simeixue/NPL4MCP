# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/common_api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools.GetAPIInfo
# lines: 54-62
def GetAPIInfo(
        service: str = Field(description='AlibabaCloud service code'),
        api: str = Field(description='AlibabaCloud api name'),
):
    """
    Use PromptUnderstanding tool first to understand the user's query, After specifying the service name and API name, get the detailed API META of the corresponding API
    """
    data, version = ApiMetaClient.get_api_meta(service, api)
    return data.get('parameters')