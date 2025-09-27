# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_get_cms_metric_data_empty_instance_ids
# lines: 82-93
def test_get_cms_metric_data_empty_instance_ids():
    # instance_ids 为空
    class FakeResp:
        class Body:
            datapoints = []
        body = Body()
    class FakeClient:
        def describe_metric_last(self, req):
            return FakeResp()
    with patch('alibaba_cloud_ops_mcp_server.tools.cms_tools.create_client', return_value=FakeClient()):
        result = cms_tools._get_cms_metric_data('cn-test', [], 'cpu_total')
        assert result == []