# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_standard_service_and_api
# lines: 67-77
    def get_standard_service_and_api(cls, service, api=None, version=None):
        data = cls.get_response_from_pop_api(cls.GET_PRODUCT_LIST)
        service_standard = (next((item.get(CODE) for item in data if item.get(CODE).lower() == service), None))
        api_standard = None
        if api:
            apis = cls.get_response_from_pop_api(cls.GET_API_OVERVIEW, service=service_standard,
                                                 version=version).get(APIS, {})
            for api_name in apis:
                if api_name.lower() == api.lower():
                    api_standard = api_name
        return service_standard, api_standard