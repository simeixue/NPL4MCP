# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_get_exposure_filters_unique_ids
# lines: 487-491
def test_get_exposure_filters_unique_ids(exposures_fetcher):
    filters = exposures_fetcher._get_exposure_filters(
        unique_ids=["exposure.test.test_exposure"]
    )
    assert filters == {"uniqueIds": ["exposure.test.test_exposure"]}