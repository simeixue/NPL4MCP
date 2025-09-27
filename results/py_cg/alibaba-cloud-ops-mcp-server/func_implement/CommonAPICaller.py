# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/common_api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools.CommonAPICaller
# lines: 66-74
def CommonAPICaller(
        service: str = Field(description='AlibabaCloud service code'),
        api: str = Field(description='AlibabaCloud api name'),
        parameters: dict = Field(description='AlibabaCloud ECS instance ID List', default={}),
):
    """
    Use PromptUnderstanding tool first to understand the user's query, Perform the actual call by specifying the Service, API, and Parameters
    """
    return _tools_api_call(service, api, parameters, None)