# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app._get_all_accounts
# lines: 28-40
def _get_all_accounts(
    *,
    dbt_platform_url: str,
    headers: dict[str, str],
) -> list[DbtPlatformAccount]:
    accounts_response = requests.get(
        url=f"{dbt_platform_url}/api/v3/accounts/",
        headers=headers,
    )
    accounts_response.raise_for_status()
    return [
        DbtPlatformAccount(**account) for account in accounts_response.json()["data"]
    ]