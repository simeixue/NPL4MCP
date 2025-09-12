# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app.create_app.oauth_callback
# lines: 144-189
    def oauth_callback(request: Request) -> RedirectResponse:
        logger.info("OAuth callback received")
        # Only handle OAuth callback when provider returns with code or error.
        params = request.query_params
        if "error" in params:
            return RedirectResponse(url="/index.html#status=error", status_code=302)
        if "code" not in params:
            return RedirectResponse(url="/index.html", status_code=302)
        state = params.get("state")
        if not state:
            logger.error("Missing state in OAuth callback")
            return RedirectResponse(url="/index.html#status=error", status_code=302)
        try:
            logger.info("Fetching access token")
            code_verifier = state_to_verifier.pop(state, None)
            if not code_verifier:
                logger.error("No code_verifier found for provided state")
                return RedirectResponse(url="/index.html#status=error", status_code=302)
            access_token_response = AccessTokenResponse(
                **oauth_client.fetch_token(
                    url=f"{dbt_platform_url}/oauth/token",
                    authorization_response=str(request.url),
                    code_verifier=code_verifier,
                )
            )
            logger.info("Access token fetched successfully")
            decoded_claims = _fetch_jwks_and_verify_token(
                access_token_response.access_token, dbt_platform_url
            )
            logger.info("JWT token verified successfully")
            app.state.decoded_access_token = DecodedAccessToken(
                access_token_response=access_token_response,
                decoded_claims=decoded_claims,
            )
            _update_dbt_platform_context(
                DbtPlatformContext(
                    decoded_access_token=app.state.decoded_access_token,
                )
            )
            return RedirectResponse(
                url="/index.html#status=success",
                status_code=302,
            )
        except Exception:
            logger.exception("OAuth callback failed")
            return RedirectResponse(url="/index.html#status=error", status_code=302)