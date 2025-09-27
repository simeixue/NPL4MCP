# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_api_meta
# lines: 80-91
    def get_api_meta(cls, service, api):
        service = service.lower()
        # API_META不包含ROA类型的API，需要通过POP平台的API GetProductList获取Service对应的Version
        # 获取POP平台API META参考文档：https://api.aliyun.com/openmeta/guide
        version = cls.get_service_version(service)
        service_standard, api_standard = cls.get_standard_service_and_api(service, api, version)
        if service_standard is None:
            raise Exception(f'InvalidServiceName: Please check the Service ({service}) you provide.')
        if api_standard is None:
            raise Exception(f'InvalidAPIName: Please check the Service ({service}) and the API ({api}) you provide.')
        data = cls.get_response_from_pop_api(cls.GET_API_INFO, service_standard, api_standard, version)
        return data, version