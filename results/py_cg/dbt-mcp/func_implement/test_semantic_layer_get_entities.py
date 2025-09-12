# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.test_semantic_layer_get_entities
# lines: 124-128
def test_semantic_layer_get_entities(semantic_layer_fetcher: SemanticLayerFetcher):
    entities = semantic_layer_fetcher.get_entities(
        metrics=["count_dbt_copilot_requests"]
    )
    assert len(entities) > 0