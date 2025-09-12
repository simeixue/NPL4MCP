# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.test_semantic_layer_what_percentage_of_orders_were_large
# lines: 249-265
async def test_semantic_layer_what_percentage_of_orders_were_large():
    tools = await get_tools()
    messages = initial_messages(
        "What percentage of orders were large this year?",
    )
    await expect_metadata_tool_call(
        messages,
        tools,
        "list_metrics",
        "{}",
    )
    expect_query_metrics_tool_call(
        messages=messages,
        tools=tools,
        expected_metrics=["orders", "large_orders"],
        expected_where="metric_time >= '2024-01-01' and metric_time < '2025-01-01'",
    )