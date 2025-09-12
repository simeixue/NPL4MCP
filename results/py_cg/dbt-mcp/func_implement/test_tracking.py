# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/tracking/test_tracking.py
# module: tests.integration.tracking.test_tracking
# qname: tests.integration.tracking.test_tracking.test_tracking
# lines: 9-12
async def test_tracking():
    config = load_config()
    await (await create_dbt_mcp(config)).call_tool("list_metrics", {"foo": "bar"})
    shutdown()