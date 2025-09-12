# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app.create_app.projects
# lines: 200-221
    def projects() -> list[DbtPlatformProject]:
        if app.state.decoded_access_token is None:
            raise RuntimeError("Access token missing; OAuth flow not completed")
        access_token = app.state.decoded_access_token.access_token_response.access_token
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        accounts = _get_all_accounts(
            dbt_platform_url=dbt_platform_url,
            headers=headers,
        )
        projects: list[DbtPlatformProject] = []
        for account in [a for a in accounts if a.state == 1 and not a.locked]:
            projects.extend(
                _get_all_projects_for_account(
                    dbt_platform_url=dbt_platform_url,
                    account=account,
                    headers=headers,
                )
            )
        return projects