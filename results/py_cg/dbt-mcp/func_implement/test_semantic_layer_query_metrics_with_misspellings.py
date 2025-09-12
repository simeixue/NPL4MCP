# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.test_semantic_layer_query_metrics_with_misspellings
# lines: 116-121
def test_semantic_layer_query_metrics_with_misspellings(
    semantic_layer_fetcher: SemanticLayerFetcher,
):
    result = semantic_layer_fetcher.query_metrics(["revehue"])
    assert result.result is not None
    assert "revenue" in result.result