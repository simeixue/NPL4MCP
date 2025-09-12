# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.test_semantic_layer_query_metrics_with_group_by_grain
# lines: 83-96
def test_semantic_layer_query_metrics_with_group_by_grain(
    semantic_layer_fetcher: SemanticLayerFetcher,
):
    result = semantic_layer_fetcher.query_metrics(
        metrics=["revenue"],
        group_by=[
            GroupByParam(
                name="metric_time",
                type=GroupByType.TIME_DIMENSION,
                grain="day",
            )
        ],
    )
    assert result is not None