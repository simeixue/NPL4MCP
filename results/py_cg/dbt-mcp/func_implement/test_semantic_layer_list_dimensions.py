# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.test_semantic_layer_list_dimensions
# lines: 31-34
def test_semantic_layer_list_dimensions(semantic_layer_fetcher: SemanticLayerFetcher):
    metrics = semantic_layer_fetcher.list_metrics()
    dimensions = semantic_layer_fetcher.get_dimensions(metrics=[metrics[0].name])
    assert len(dimensions) > 0