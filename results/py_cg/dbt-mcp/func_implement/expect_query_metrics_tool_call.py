# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.expect_query_metrics_tool_call
# lines: 75-136
def expect_query_metrics_tool_call(
    messages: list,
    tools: list[FunctionToolParam],
    expected_metrics: list[str],
    expected_group_by: list[dict] | None = None,
    expected_order_by: list[dict] | None = None,
    expected_where: str | None = None,
    expected_limit: int | None = None,
):
    response = llm_client.responses.create(
        model=LLM_MODEL,
        input=messages,
        tools=tools,
        parallel_tool_calls=False,
    )
    assert len(response.output) == 1
    tool_call = response.output[0]
    assert isinstance(tool_call, ResponseFunctionToolCall)
    assert tool_call.name == "query_metrics"
    args_dict = json.loads(tool_call.arguments)
    assert set(args_dict["metrics"]) == set(expected_metrics)
    if expected_group_by is not None:
        assert deep_equal(args_dict["group_by"], expected_group_by)
    else:
        assert args_dict.get("group_by", []) == []
    if expected_order_by is not None:
        assert deep_equal(args_dict["order_by"], expected_order_by)
    else:
        assert args_dict.get("order_by", []) == []
    if expected_where is not None:
        assert args_dict["where"] == expected_where
    else:
        assert args_dict.get("where", None) is None
    if expected_limit is not None:
        assert args_dict["limit"] == expected_limit
    else:
        assert args_dict.get("limit", None) is None

    sl_config = config.semantic_layer_config
    assert sl_config is not None
    semantic_layer_fetcher = SemanticLayerFetcher(
        sl_client=SyncSemanticLayerClient(
            environment_id=sl_config.prod_environment_id,
            auth_token=sl_config.service_token,
            host=sl_config.host,
        ),
        config=sl_config,
    )
    tool_response = semantic_layer_fetcher.query_metrics(
        metrics=args_dict["metrics"],
        group_by=[
            GroupByParam(name=g["name"], type=g["type"], grain=g.get("grain"))
            for g in args_dict.get("group_by", [])
        ],
        order_by=[
            OrderByParam(name=o["name"], descending=o["descending"])
            for o in args_dict.get("order_by", [])
        ],
        where=args_dict.get("where"),
        limit=args_dict.get("limit"),
    )
    assert isinstance(tool_response, QueryMetricsSuccess)