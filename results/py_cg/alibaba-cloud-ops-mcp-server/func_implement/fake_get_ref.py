# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_api_parameters_circular_ref.fake_get_ref
# lines: 101-102
    def fake_get_ref(data, service, version):
        return {'$ref': '#/defs/foo'}