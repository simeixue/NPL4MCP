# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/login.py
# module: src.dbt_mcp.oauth.login
# qname: src.dbt_mcp.oauth.login.login
# lines: 18-90
def login(
    *,
    dbt_platform_url: str,
    port: int,
    client_id: str,
    config_location: Path,
) -> DbtPlatformContext:
    """Start OAuth login flow with PKCE using authlib and return
    the decoded access token
    """
    # OAuth2 configuration
    redirect_uri = f"http://localhost:{port}"
    authorization_endpoint = f"{dbt_platform_url}/oauth/authorize"

    # 'offline_access' scope indicates that we want to request a refresh token
    # 'user_access' is equivalent to a PAT
    scope = "user_access offline_access"

    # Create OAuth2Session with PKCE support
    client = OAuth2Session(
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        code_challenge_method="S256",
    )

    # Generate code_verifier
    code_verifier = secrets.token_urlsafe(32)

    # Generate authorization URL with PKCE
    authorization_url, state = client.create_authorization_url(
        url=authorization_endpoint,
        code_verifier=code_verifier,
    )

    try:
        # Resolve static assets directory from package
        package_root = resources.files("dbt_mcp")
        packaged_dist = package_root / "ui" / "dist"
        if not packaged_dist.is_dir():
            raise FileNotFoundError(f"{packaged_dist} not found in packaged resources")
        static_dir = str(packaged_dist)

        # Create FastAPI app and Uvicorn server
        app = create_app(
            oauth_client=client,
            state_to_verifier={state: code_verifier},
            dbt_platform_url=dbt_platform_url,
            static_dir=static_dir,
            config_location=config_location,
        )
        config = Config(
            app=app,
            host="127.0.0.1",
            port=port,
        )
        server = Server(config)
        app.state.server_ref = server

        logger.info("Opening authorization URL")
        webbrowser.open(authorization_url)
        # Logs have to be disabled because they mess up stdio MCP communication
        disable_server_logs()
        server.run()

        if not app.state.dbt_platform_context:
            raise ValueError("Undefined login state")
        logger.info("Login successful")
        return app.state.dbt_platform_context
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            logger.error(f"Error: Port {port} is already in use.")
        raise