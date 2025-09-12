# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.test_semantic_layer_list_metrics
# lines: 26-28
def test_semantic_layer_list_metrics(semantic_layer_fetcher: SemanticLayerFetcher):
    metrics = semantic_layer_fetcher.list_metrics()
    assert len(metrics) > 0