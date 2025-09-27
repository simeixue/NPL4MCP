# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.fake_client
# lines: 8-28
def fake_client(*args, **kwargs):
    class FakeExecution:
        execution_id = 'exec-1'
        status = 'Success'
        status_message = 'ok'
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
    return FakeClient()