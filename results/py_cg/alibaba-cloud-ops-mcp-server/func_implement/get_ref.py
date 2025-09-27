# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/api_meta_client.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.api_meta_client.ApiMetaClient.get_api_parameters.get_ref
# lines: 125-142
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