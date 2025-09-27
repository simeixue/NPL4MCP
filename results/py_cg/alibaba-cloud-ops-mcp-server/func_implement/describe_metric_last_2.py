# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_get_cms_metric_data_client_exception.FakeClient.describe_metric_last
# lines: 97-98
        def describe_metric_last(self, req):
            raise Exception('fail-metric')