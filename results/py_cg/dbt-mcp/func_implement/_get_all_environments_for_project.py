# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app._get_all_environments_for_project
# lines: 69-93
def _get_all_environments_for_project(
    *,
    dbt_platform_url: str,
    account_id: int,
    project_id: int,
    headers: dict[str, str],
    page_size: int = 100,
) -> list[DbtPlatformEnvironmentResponse]:
    """Fetch all environments for a project using offset/page_size pagination."""
    offset = 0
    environments: list[DbtPlatformEnvironmentResponse] = []
    while True:
        environments_response = requests.get(
            f"{dbt_platform_url}/api/v3/accounts/{account_id}/projects/{project_id}/environments/?state=1&offset={offset}&limit={page_size}",
            headers=headers,
        )
        environments_response.raise_for_status()
        page = environments_response.json()["data"]
        environments.extend(
            DbtPlatformEnvironmentResponse(**environment) for environment in page
        )
        if len(page) < page_size:
            break
        offset += page_size
    return environments