# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_get_cms_metric_data_client_exception
# lines: 95-102
def test_get_cms_metric_data_client_exception():
    class FakeClient:
        def describe_metric_last(self, req):
            raise Exception('fail-metric')
    with patch('alibaba_cloud_ops_mcp_server.tools.cms_tools.create_client', return_value=FakeClient()):
        with pytest.raises(Exception) as e:
            cms_tools._get_cms_metric_data('cn-test', ['i-1'], 'cpu_total')
        assert 'fail-metric' in str(e.value)