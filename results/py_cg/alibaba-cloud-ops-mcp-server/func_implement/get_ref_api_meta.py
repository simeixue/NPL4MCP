# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_ref_api_meta
# lines: 100-111
    def get_ref_api_meta(cls, data, service, version):
        service_standard, _ = cls.get_standard_service_and_api(service=service, version=version)
        current_data = cls.get_response_from_pop_api(cls.GET_API_OVERVIEW, service=service_standard, version=version)
        ref_path = data.get(REF)
        path = ref_path.lstrip('#/').split('/')
        for _key in path:
            if _key in current_data:
                current_data = current_data[_key]
            else:
                raise KeyError(f"Path {_key} not found in the JSON data.")

        return current_data