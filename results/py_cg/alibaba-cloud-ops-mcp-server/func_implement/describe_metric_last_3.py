# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_get_cms_metric_data_multiple_instance_ids.FakeClient.describe_metric_last
# lines: 111-117
        def describe_metric_last(self, req):
            # 检查 dimensions 是否包含多个 instanceId
            dims = json.loads(req.dimensions)
            assert isinstance(dims, list)
            assert {'instanceId': 'i-1'} in dims
            assert {'instanceId': 'i-2'} in dims
            return FakeResp()