# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.test_semantic_layer_query_metrics_invalid_query
# lines: 51-80
def test_semantic_layer_query_metrics_invalid_query(
    semantic_layer_fetcher: SemanticLayerFetcher,
):
    result = semantic_layer_fetcher.query_metrics(
        metrics=["food_revenue"],
        group_by=[
            GroupByParam(
                name="order_id__location__location_name",
                type=GroupByType.DIMENSION,
                grain=None,
            ),
            GroupByParam(
                name="metric_time",
                type=GroupByType.TIME_DIMENSION,
                grain="MONTH",
            ),
        ],
        order_by=[
            OrderByParam(
                name="metric_time",
                descending=True,
            ),
            OrderByParam(
                name="food_revenue",
                descending=True,
            ),
        ],
        limit=5,
    )
    assert result is not None