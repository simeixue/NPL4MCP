# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_model_parents_with_uniqueId
# lines: 119-135
def test_fetch_model_parents_with_uniqueId(models_fetcher: ModelsFetcher):
    models = models_fetcher.fetch_models()
    model = models[0]
    model_name = model["name"]
    unique_id = model["uniqueId"]

    # Fetch by name
    results_by_name = models_fetcher.fetch_model_parents(model_name)

    # Fetch by uniqueId
    results_by_uniqueId = models_fetcher.fetch_model_parents(model_name, unique_id)

    # Validate that both methods return the same result
    assert len(results_by_name) == len(results_by_uniqueId)
    if len(results_by_name) > 0:
        # Compare the first parent's name if there are any parents
        assert results_by_name[0]["name"] == results_by_uniqueId[0]["name"]