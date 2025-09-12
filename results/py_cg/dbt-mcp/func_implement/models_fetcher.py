# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.models_fetcher
# lines: 30-35
def models_fetcher(api_client: MetadataAPIClient) -> ModelsFetcher:
    environment_id = os.getenv("DBT_PROD_ENV_ID")
    if not environment_id:
        raise ValueError("DBT_PROD_ENV_ID environment variable is required")

    return ModelsFetcher(api_client=api_client, environment_id=int(environment_id))