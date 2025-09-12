# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app._get_all_projects_for_account
# lines: 43-66
def _get_all_projects_for_account(
    *,
    dbt_platform_url: str,
    account: DbtPlatformAccount,
    headers: dict[str, str],
    page_size: int = 100,
) -> list[DbtPlatformProject]:
    """Fetch all projects for an account using offset/page_size pagination."""
    offset = 0
    projects: list[DbtPlatformProject] = []
    while True:
        projects_response = requests.get(
            f"{dbt_platform_url}/api/v3/accounts/{account.id}/projects/?state=1&offset={offset}&limit={page_size}",
            headers=headers,
        )
        projects_response.raise_for_status()
        page = projects_response.json()["data"]
        projects.extend(
            DbtPlatformProject(**project, account_name=account.name) for project in page
        )
        if len(page) < page_size:
            break
        offset += page_size
    return projects