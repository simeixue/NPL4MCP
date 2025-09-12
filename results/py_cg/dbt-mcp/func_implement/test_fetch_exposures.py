# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_exposures
# lines: 168-180
def test_fetch_exposures(exposures_fetcher: ExposuresFetcher):
    results = exposures_fetcher.fetch_exposures()

    # Basic validation of the response
    assert isinstance(results, list)

    # If there are exposures, validate their structure
    if len(results) > 0:
        for exposure in results:
            assert "name" in exposure
            assert "uniqueId" in exposure
            assert isinstance(exposure["name"], str)
            assert isinstance(exposure["uniqueId"], str)