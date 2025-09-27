# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_start_execution_sync_failed
# lines: 96-120
def test_start_execution_sync_failed():
    # FakeClient 返回 status==FAILED
    class FakeExecution:
        execution_id = 'exec-1'
        status = 'Failed'
        status_message = 'fail-reason'
    class FakeBody:
        executions = [FakeExecution()]
    class FakeListResp:
        body = FakeBody()
    class FakeStartResp:
        class Body:
            class Execution:
                execution_id = 'exec-1'
            execution = Execution()
        body = Body()
    class FakeClient:
        def start_execution(self, req):
            return FakeStartResp()
        def list_executions(self, req):
            return FakeListResp()
    with patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.create_client', return_value=FakeClient()):
        with pytest.raises(Exception) as e:
            oos_tools._start_execution_sync('cn-test', 'tpl', {})
        assert 'fail-reason' in str(e.value)