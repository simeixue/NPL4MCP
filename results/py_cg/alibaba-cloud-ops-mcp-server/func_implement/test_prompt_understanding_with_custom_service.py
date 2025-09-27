# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_prompt_understanding_with_custom_service
# lines: 338-344
def test_prompt_understanding_with_custom_service():
    # _CUSTOM_SERVICE_LIST 有值
    import alibaba_cloud_ops_mcp_server.tools.common_api_tools as ca
    ca._CUSTOM_SERVICE_LIST = [('ecs', 'ECS服务'), ('rds', 'RDS服务')]
    fn = ca.tools[0]  # PromptUnderstanding
    result = fn()
    assert 'ecs: ECS服务' in result and 'rds: RDS服务' in result