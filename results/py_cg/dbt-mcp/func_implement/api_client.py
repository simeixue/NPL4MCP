# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/discovery/test_discovery.py
# module: tests.integration.discovery.test_discovery
# qname: tests.integration.discovery.test_discovery.api_client
# lines: 14-26
def api_client() -> MetadataAPIClient:
    host = os.getenv("DBT_HOST")
    token = os.getenv("DBT_TOKEN")

    if not host or not token:
        raise ValueError("DBT_HOST and DBT_TOKEN environment variables are required")
    return MetadataAPIClient(
        url=f"https://metadata.{host}/graphql",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )