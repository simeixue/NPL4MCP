# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_response_from_api_meta
# lines: 94-97
    def get_response_from_api_meta(cls, service, api):
        api_meta, version = cls.get_api_meta(service, api)
        property_values = api_meta.get(RESPONSES, {}).get(HTTP_SUCCESS_CODE, {}).get(SCHEMA, {}).get(PROPERTIES, {})
        return property_values, version