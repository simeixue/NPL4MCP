# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oss_tools.py
# module: tests.tools.test_oss_tools
# qname: tests.tools.test_oss_tools.fake_client
# lines: 8-24
def fake_client(*args, **kwargs):
    class FakePaginator:
        def iter_page(self, req):
            class Page:
                buckets = [MagicMock(__str__=lambda self: 'bucket1')]
                contents = [MagicMock(__str__=lambda self: 'obj1')]
            yield Page()
    class FakeClient:
        def list_buckets_paginator(self):
            return FakePaginator()
        def list_objects_v2_paginator(self):
            return FakePaginator()
        def put_bucket(self, req):
            return MagicMock(__str__=lambda self: 'put_bucket')
        def delete_bucket(self, req):
            return MagicMock(__str__=lambda self: 'delete_bucket')
    return FakeClient()