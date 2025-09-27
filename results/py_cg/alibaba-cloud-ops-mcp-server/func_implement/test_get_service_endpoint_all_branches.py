# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_get_service_endpoint_all_branches
# lines: 379-388
def test_get_service_endpoint_all_branches():
    from alibaba_cloud_ops_mcp_server.tools.api_tools import _get_service_endpoint
    # REGION_ENDPOINT_SERVICE 分支
    assert _get_service_endpoint('ecs', 'cn-hangzhou') == 'ecs.cn-hangzhou.aliyuncs.com'
    # DOUBLE_ENDPOINT_SERVICE 且 region 匹配
    assert _get_service_endpoint('rds', 'cn-hangzhou') == 'rds.aliyuncs.com'
    # CENTRAL_ENDPOINTS_SERVICE 分支
    assert _get_service_endpoint('cbn', 'cn-hangzhou') == 'cbn.aliyuncs.com'
    # 其它分支
    assert _get_service_endpoint('unknown', 'cn-test') == 'unknown.cn-test.aliyuncs.com'