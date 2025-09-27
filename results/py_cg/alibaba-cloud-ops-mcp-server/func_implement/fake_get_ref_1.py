# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_nested_ref.fake_get_ref
# lines: 266-271
    def fake_get_ref(data, service, version):
        if '#/defs/A' in data.get('$ref', ''):
            return {'properties': {'a': {'$ref': '#/defs/B'}}}
        elif '#/defs/B' in data.get('$ref', ''):
            return {'properties': {'b': {}}}
        return {}