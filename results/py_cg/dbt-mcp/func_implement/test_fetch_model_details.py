# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_model_details
# lines: 80-88
def test_fetch_model_details(models_fetcher: ModelsFetcher):
    models = models_fetcher.fetch_models()
    model_name = models[0]["name"]

    # Fetch filtered results
    filtered_results = models_fetcher.fetch_model_details(model_name)

    # Validate filtered results
    assert len(filtered_results) > 0