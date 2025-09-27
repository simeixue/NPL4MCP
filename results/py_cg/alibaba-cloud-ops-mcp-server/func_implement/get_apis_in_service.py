# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_apis_in_service
# lines: 157-161
    def get_apis_in_service(cls, service):
        version = cls.get_service_version(service)
        data = cls.get_response_from_pop_api(cls.GET_API_OVERVIEW, service=service, version=version)
        apis = list(data[APIS].keys())
        return apis