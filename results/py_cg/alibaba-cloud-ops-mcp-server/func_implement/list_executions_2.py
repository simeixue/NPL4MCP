# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_start_execution_sync_loop.FakeClient.list_executions
# lines: 143-157
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