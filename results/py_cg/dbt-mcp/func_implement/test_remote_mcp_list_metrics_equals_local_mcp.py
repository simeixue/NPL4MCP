# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/remote_mcp/test_remote_mcp.py
# module: tests.integration.remote_mcp.test_remote_mcp
# qname: tests.integration.remote_mcp.test_remote_mcp.test_remote_mcp_list_metrics_equals_local_mcp
# lines: 6-19
async def test_remote_mcp_list_metrics_equals_local_mcp() -> None:
    async with session_context() as session:
        config = load_config()
        dbt_mcp = await create_dbt_mcp(config)

        remote_metrics = await session.call_tool(
            name="list_metrics",
            arguments={},
        )
        local_metrics = await dbt_mcp.call_tool(
            name="list_metrics",
            arguments={},
        )
        assert remote_metrics.content == local_metrics