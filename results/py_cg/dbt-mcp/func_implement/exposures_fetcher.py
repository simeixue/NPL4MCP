# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.exposures_fetcher
# lines: 13-14
def exposures_fetcher(mock_api_client):
    return ExposuresFetcher(api_client=mock_api_client, environment_id=123)