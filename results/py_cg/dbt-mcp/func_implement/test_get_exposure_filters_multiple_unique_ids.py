# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_get_exposure_filters_multiple_unique_ids
# lines: 494-498
def test_get_exposure_filters_multiple_unique_ids(exposures_fetcher):
    filters = exposures_fetcher._get_exposure_filters(
        unique_ids=["exposure.test.test1", "exposure.test.test2"]
    )
    assert filters == {"uniqueIds": ["exposure.test.test1", "exposure.test.test2"]}