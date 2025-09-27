# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_api_parameters
# lines: 114-154
    def get_api_parameters(cls, service, api, params_in=''):
        """
        params_in: 过滤参数位置，取值：'host', 'query', 'body', 'header'，若为空，则返回所有参数
        """
        api_meta, _ = cls.get_api_meta(service, api)
        parameters = api_meta.get(PARAMETERS)
        param_names = []
        additional_props = []
        # 避免循环引用
        visited_refs = set()

        def get_ref(data, _):
            props = []
            if not isinstance(data, dict):
                return props
            if REF in data:
                ref_path = data.get(REF)
                if ref_path in visited_refs:
                    return props
                visited_refs.add(ref_path)
                referenced_schema = cls.get_ref_api_meta(data, service, _)
                props.extend(get_ref(referenced_schema, _))
                return props
            if PROPERTIES in data:
                for prop_name, prop_details in data.get(PROPERTIES, {}).items():
                    props.append(prop_name)
                    if isinstance(prop_details, dict) and REF in prop_details:
                        props.extend(get_ref(prop_details, _))
            return props

        for param in parameters:
            if params_in and param.get(IN) != params_in:
                continue
            param_name = param.get(NAME)
            if param_name:
                param_names.append(param_name)
            schema = param.get(SCHEMA, {})
            extracted_props = get_ref(schema, _)
            additional_props.extend(extracted_props)
        combined_params = param_names + additional_props
        return combined_params