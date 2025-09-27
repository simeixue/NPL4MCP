# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oos_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oos_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oos_tools._start_execution_sync
# lines: 25-47
def _start_execution_sync(region_id: str, template_name: str, parameters: dict):
    client = create_client(region_id=region_id)
    start_execution_request = oos_20190601_models.StartExecutionRequest(
        region_id=region_id,
        template_name=template_name,
        parameters=json.dumps(parameters)
    )
    start_execution_resp = client.start_execution(start_execution_request)
    execution_id = start_execution_resp.body.execution.execution_id

    while True:
        list_executions_request = oos_20190601_models.ListExecutionsRequest(
            region_id=region_id,
            execution_id=execution_id
        )
        list_executions_resp = client.list_executions(list_executions_request)
        status = list_executions_resp.body.executions[0].status
        if status == FAILED:
            status_message = list_executions_resp.body.executions[0].status_message
            raise exception.OOSExecutionFailed(reason=status_message)
        elif status in END_STATUSES:
            return list_executions_resp.body
        time.sleep(1)