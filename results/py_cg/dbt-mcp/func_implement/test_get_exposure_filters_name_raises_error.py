# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_get_exposure_filters_name_raises_error
# lines: 501-503
def test_get_exposure_filters_name_raises_error(exposures_fetcher):
    with pytest.raises(ValueError, match="ExposureFilter only supports uniqueIds"):
        exposures_fetcher._get_exposure_filters(exposure_name="test_exposure")