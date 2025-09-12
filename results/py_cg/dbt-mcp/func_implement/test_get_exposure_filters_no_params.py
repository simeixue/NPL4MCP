# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_get_exposure_filters_no_params
# lines: 506-510
def test_get_exposure_filters_no_params(exposures_fetcher):
    with pytest.raises(
        ValueError, match="unique_ids must be provided for exposure filtering"
    ):
        exposures_fetcher._get_exposure_filters()