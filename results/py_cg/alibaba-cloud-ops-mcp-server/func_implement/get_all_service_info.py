# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_all_service_info
# lines: 54-58
    def get_all_service_info(cls):
        data = cls.get_response_from_pop_api(cls.GET_PRODUCT_LIST)
        filtered_data = [{"code": item["code"], "name": item["name"]} for item in data]

        return filtered_data