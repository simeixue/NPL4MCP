# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_model_details_with_uniqueId
# lines: 91-105
def test_fetch_model_details_with_uniqueId(models_fetcher: ModelsFetcher):
    models = models_fetcher.fetch_models()
    model = models[0]
    model_name = model["name"]
    unique_id = model["uniqueId"]

    # Fetch by name
    results_by_name = models_fetcher.fetch_model_details(model_name)

    # Fetch by uniqueId
    results_by_uniqueId = models_fetcher.fetch_model_details(model_name, unique_id)

    # Validate that both methods return the same result
    assert results_by_name["uniqueId"] == results_by_uniqueId["uniqueId"]
    assert results_by_name["name"] == results_by_uniqueId["name"]