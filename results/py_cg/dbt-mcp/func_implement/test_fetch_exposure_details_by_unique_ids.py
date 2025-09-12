# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.test_fetch_exposure_details_by_unique_ids
# lines: 200-228
def test_fetch_exposure_details_by_unique_ids(exposures_fetcher: ExposuresFetcher):
    # First get all exposures to find one to test with
    exposures = exposures_fetcher.fetch_exposures()

    # Skip test if no exposures are available
    if not exposures:
        pytest.skip("No exposures available in the test environment")

    # Pick the first exposure to test with
    test_exposure = exposures[0]
    unique_id = test_exposure["uniqueId"]

    # Fetch the same exposure by unique_ids
    result = exposures_fetcher.fetch_exposure_details(unique_ids=[unique_id])

    # Validate that we got the correct exposure back
    assert isinstance(result, list)
    assert len(result) == 1
    exposure = result[0]
    assert exposure["uniqueId"] == unique_id
    assert exposure["name"] == test_exposure["name"]
    assert "exposureType" in exposure
    assert "maturity" in exposure

    # Validate structure
    if "parents" in exposure and exposure["parents"]:
        assert isinstance(exposure["parents"], list)
        for parent in exposure["parents"]:
            assert "uniqueId" in parent