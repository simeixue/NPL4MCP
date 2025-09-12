# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.test_semantic_layer_food_revenue_per_month
# lines: 201-246
async def test_semantic_layer_food_revenue_per_month():
    tools = await get_tools()
    messages = initial_messages(
        "What is our food revenue per location per month?",
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
        '{"metrics":["food_revenue"]}',
    )
    await expect_metadata_tool_call(
        messages,
        tools,
        "get_entities",
        '{"metrics":["food_revenue"]}',
    )
    expect_query_metrics_tool_call(
        messages=messages,
        tools=tools,
        expected_metrics=["food_revenue"],
        expected_group_by=[
            {
                "name": "order_id__location__location_name",
                "type": "entity",
            },
            {
                "name": "metric_time",
                "type": "time_dimension",
                "grain": "MONTH",
            },
        ],
        expected_order_by=[
            {
                "name": "metric_time",
                "descending": True,
            },
        ],
        expected_limit=5,
    )