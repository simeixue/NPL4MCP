# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_exception.py
# module: tests.alibabacloud.test_exception
# qname: tests.alibabacloud.test_exception.test_acs_exception_default
# lines: 4-12
def test_acs_exception_default():
    e = exception.AcsException()
    s = str(e)
    assert 'InternalError' in s
    assert 'unknown exception' in s.lower()
    assert e.status == 500
    assert e.code == 'InternalError'
    assert isinstance(e.__deepcopy__({}), exception.AcsException)
    assert isinstance(e.__unicode__(), str)