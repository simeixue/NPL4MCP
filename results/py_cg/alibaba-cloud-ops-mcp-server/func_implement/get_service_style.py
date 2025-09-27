# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_service_style
# lines: 61-64
    def get_service_style(cls, service):
        data = cls.get_response_from_pop_api(cls.GET_PRODUCT_LIST)
        style = next((item.get(STYLE) for item in data if item.get(CODE).lower() == service), 'RPC')
        return style