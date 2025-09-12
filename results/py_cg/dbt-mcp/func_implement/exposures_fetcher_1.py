# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.exposures_fetcher
# lines: 39-44
def exposures_fetcher(api_client: MetadataAPIClient) -> ExposuresFetcher:
    environment_id = os.getenv("DBT_PROD_ENV_ID")
    if not environment_id:
        raise ValueError("DBT_PROD_ENV_ID environment variable is required")

    return ExposuresFetcher(api_client=api_client, environment_id=int(environment_id))