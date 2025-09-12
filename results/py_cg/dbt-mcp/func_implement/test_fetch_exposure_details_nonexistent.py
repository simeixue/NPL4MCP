# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_exposure_details_nonexistent
# lines: 231-238
def test_fetch_exposure_details_nonexistent(exposures_fetcher: ExposuresFetcher):
    # Test with a non-existent exposure
    result = exposures_fetcher.fetch_exposure_details(
        unique_ids=["exposure.nonexistent.exposure"]
    )

    # Should return empty list when not found
    assert result == []