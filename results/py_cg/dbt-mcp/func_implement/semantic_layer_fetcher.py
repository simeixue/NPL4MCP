# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/semantic_layer/test_semantic_layer.py
# module: tests.integration.semantic_layer.test_semantic_layer
# qname: tests.integration.semantic_layer.test_semantic_layer.semantic_layer_fetcher
# lines: 13-23
def semantic_layer_fetcher() -> SemanticLayerFetcher:
    sl_config = config.semantic_layer_config
    assert sl_config is not None
    return SemanticLayerFetcher(
        sl_client=SyncSemanticLayerClient(
            environment_id=sl_config.prod_environment_id,
            auth_token=sl_config.service_token,
            host=sl_config.host,
        ),
        config=sl_config,
    )