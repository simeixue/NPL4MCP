# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_exception.py
# module: tests.alibabacloud.test_exception
# qname: tests.alibabacloud.test_exception.test_acs_exception_format
# lines: 14-20
def test_acs_exception_format():
    class CustomEx(exception.AcsException):
        msg_fmt = 'Error: {foo}.'
        code = 'CustomError'
    e = CustomEx(foo='bar')
    assert 'bar' in str(e)
    assert 'CustomError' in str(e)