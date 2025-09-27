# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.fake_client.FakeClient.put_bucket
# lines: 20-21
        def put_bucket(self, req):
            return MagicMock(__str__=lambda self: 'put_bucket')