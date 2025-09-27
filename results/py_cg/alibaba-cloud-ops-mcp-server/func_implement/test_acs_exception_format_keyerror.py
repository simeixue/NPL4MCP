# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_exception.py
# module: tests.alibabacloud.test_exception
# qname: tests.alibabacloud.test_exception.test_acs_exception_format_keyerror
# lines: 22-28
def test_acs_exception_format_keyerror(caplog):
    class CustomEx(exception.AcsException):
        msg_fmt = 'Error: {foo}.'
        code = 'CustomError'
    with caplog.at_level('ERROR'):
        e = CustomEx(badkey='baz')
        assert 'badkey' in caplog.text