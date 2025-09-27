# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_get_cms_metric_data_multiple_instance_ids
# lines: 104-120
def test_get_cms_metric_data_multiple_instance_ids():
    # instance_ids 有多个元素，覆盖 for 循环
    class FakeResp:
        class Body:
            datapoints = [{'value': 1}, {'value': 2}]
        body = Body()
    class FakeClient:
        def describe_metric_last(self, req):
            # 检查 dimensions 是否包含多个 instanceId
            dims = json.loads(req.dimensions)
            assert isinstance(dims, list)
            assert {'instanceId': 'i-1'} in dims
            assert {'instanceId': 'i-2'} in dims
            return FakeResp()
    with patch('alibaba_cloud_ops_mcp_server.tools.cms_tools.create_client', return_value=FakeClient()):
        result = cms_tools._get_cms_metric_data('cn-test', ['i-1', 'i-2'], 'cpu_total')
        assert result == [{'value': 1}, {'value': 2}]