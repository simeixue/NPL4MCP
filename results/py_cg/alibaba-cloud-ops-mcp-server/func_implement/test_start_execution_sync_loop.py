# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_start_execution_sync_loop
# lines: 122-162
def test_start_execution_sync_loop():
    # status 既不是 FAILED 也不是 END_STATUSES，触发 time.sleep(1)
    class FakeExecution:
        execution_id = 'exec-1'
        status = 'Running'
        status_message = 'running'
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
        def __init__(self):
            self.calls = 0
        def start_execution(self, req):
            return FakeStartResp()
        def list_executions(self, req):
            # 前两次返回 Running，第三次返回 Success
            self.calls += 1
            if self.calls < 3:
                return FakeListResp()
            else:
                class DoneExecution:
                    execution_id = 'exec-1'
                    status = 'Success'
                    status_message = 'ok'
                class DoneBody:
                    executions = [DoneExecution()]
                class DoneListResp:
                    body = DoneBody()
                return DoneListResp()
    with patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.create_client', return_value=FakeClient()), \
         patch('time.sleep', return_value=None) as mock_sleep:
        result = oos_tools._start_execution_sync('cn-test', 'tpl', {})
        assert hasattr(result, 'executions')
        assert mock_sleep.call_count >= 1