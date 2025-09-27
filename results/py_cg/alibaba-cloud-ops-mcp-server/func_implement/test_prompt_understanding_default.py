# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_prompt_understanding_default
# lines: 329-336
def test_prompt_understanding_default():
    # _CUSTOM_SERVICE_LIST 为空
    import alibaba_cloud_ops_mcp_server.tools.common_api_tools as ca
    ca._CUSTOM_SERVICE_LIST = None
    fn = ca.tools[0]  # PromptUnderstanding
    result = fn()
    assert isinstance(result, str)
    assert 'Supported Services' in result