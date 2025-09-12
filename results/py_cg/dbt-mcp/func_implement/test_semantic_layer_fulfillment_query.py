# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.test_semantic_layer_fulfillment_query
# lines: 178-198
async def test_semantic_layer_fulfillment_query():
    tools = await get_tools()
    messages = initial_messages(
        "How many orders did we fulfill this month last year?",
    )
    await expect_metadata_tool_call(
        messages,
        tools,
        "list_metrics",
        "{}",
    )
    await expect_metadata_tool_call(
        messages,
        tools,
        "get_dimensions",
        '{"metrics":["orders"]}',
    )
    expect_query_metrics_tool_call(
        messages,
        tools,
    )