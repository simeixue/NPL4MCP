# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_exception.py
# module: tests.alibabacloud.test_exception
# qname: tests.alibabacloud.test_exception.test_oos_execution_failed
# lines: 30-36
def test_oos_execution_failed():
    e = exception.OOSExecutionFailed(reason='fail')
    s = str(e)
    assert 'OOS Execution Failed' in s
    assert 'Execution.Failed' in s
    assert e.status == 400
    assert e.code == 'Execution.Failed' 