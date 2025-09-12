# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_model_parents
# lines: 108-116
def test_fetch_model_parents(models_fetcher: ModelsFetcher):
    models = models_fetcher.fetch_models()
    model_name = models[0]["name"]

    # Fetch filtered results
    filtered_results = models_fetcher.fetch_model_parents(model_name)

    # Validate filtered results
    assert len(filtered_results) > 0