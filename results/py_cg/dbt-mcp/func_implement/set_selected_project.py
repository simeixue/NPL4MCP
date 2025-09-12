# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app.create_app.set_selected_project
# lines: 229-285
    def set_selected_project(
        selected_project_request: SelectedProjectRequest,
    ) -> DbtPlatformContext:
        logger.info("Selected project received")
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
        account = next(
            (a for a in accounts if a.id == selected_project_request.account_id), None
        )
        if account is None:
            raise ValueError(f"Account {selected_project_request.account_id} not found")
        environments = _get_all_environments_for_project(
            dbt_platform_url=dbt_platform_url,
            account_id=selected_project_request.account_id,
            project_id=selected_project_request.project_id,
            headers=headers,
            page_size=100,
        )
        prod_environment = None
        dev_environment = None
        for environment in environments:
            if (
                environment.deployment_type
                and environment.deployment_type.lower() == "production"
            ):
                prod_environment = DbtPlatformEnvironment(
                    id=environment.id,
                    name=environment.name,
                    deployment_type=environment.deployment_type,
                )
            elif (
                environment.deployment_type
                and environment.deployment_type.lower() == "development"
            ):
                dev_environment = DbtPlatformEnvironment(
                    id=environment.id,
                    name=environment.name,
                    deployment_type=environment.deployment_type,
                )
        dbt_platform_context = _update_dbt_platform_context(
            new_dbt_platform_context=DbtPlatformContext(
                decoded_access_token=app.state.decoded_access_token,
                dev_environment=dev_environment,
                prod_environment=prod_environment,
                host_prefix=account.host_prefix,
            ),
        )
        return dbt_platform_context