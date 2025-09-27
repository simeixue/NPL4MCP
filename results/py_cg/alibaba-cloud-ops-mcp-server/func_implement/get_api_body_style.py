# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_api_body_style
# lines: 172-177
    def get_api_body_style(cls, service, api):
        parameters = cls.get_api_field(PARAMETERS, service, api)
        body_style = None
        if parameters:
            body_style = next((param.get(STYLE) for param in parameters if param.get(IN) == BODY), None)
        return body_style