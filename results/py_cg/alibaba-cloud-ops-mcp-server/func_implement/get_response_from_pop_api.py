# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_response_from_pop_api
# lines: 32-45
    def get_response_from_pop_api(cls, pop_api_name, service=None, api=None, version=None):
        url = None  # 提前定义，防止 except 中引用未定义变量
        try:
            api_config = cls.config.get(pop_api_name)
            try:
                formatted_path = api_config[cls.PATH].format(service=service, api=api, version=version)
            except KeyError as e:
                raise Exception(f'Failed to format path, path: {api_config.get(cls.PATH)}, error: {e}')

            url = f'{cls.BASE_URL}/{formatted_path}'
            response = requests.get(url)
            return response.json()
        except Exception as e:
            raise Exception(f'Failed to get response from pop api, url: {url}, error: {e}')