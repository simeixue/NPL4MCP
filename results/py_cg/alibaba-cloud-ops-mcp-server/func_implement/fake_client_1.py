# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.fake_client
# lines: 9-19
def fake_client(*args, **kwargs):
    class FakeResp:
        class Body:
            datapoints = [{"value": 1}]
        body = Body()
        def __init__(self):
            pass
    class FakeClient:
        def describe_metric_last(self, req):
            return FakeResp()
    return FakeClient()