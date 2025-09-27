# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.fake_client.FakePaginator.iter_page
# lines: 10-14
        def iter_page(self, req):
            class Page:
                buckets = [MagicMock(__str__=lambda self: 'bucket1')]
                contents = [MagicMock(__str__=lambda self: 'obj1')]
            yield Page()