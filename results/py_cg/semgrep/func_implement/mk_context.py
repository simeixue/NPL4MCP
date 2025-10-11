# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.mk_context
# lines: 193-239
async def mk_context(top_level_span: trace.Span | None) -> SemgrepContext:
    """
    Runs the semgrep daemon (`semgrep mcp`) if:
    - the user has the Pro Engine installed
    - is running the MCP server locally
    - the USE_SEMGREP_RPC env var is set to true

    TODO: remove the "running locally" check once we have a way to
    obtain per-user app tokens in the hosted environment
    """
    process = None
    pro_engine_available = True

    use_rpc = os.environ.get("USE_SEMGREP_RPC", "true").lower() == "true"

    resp = await run_semgrep_process_sync(top_level_span, ["--pro", "--version"])

    # The user doesn't seem to have the Pro Engine installed.
    # That's fine, let's just run the free engine, without the
    # `semgrep mcp` backend.
    if resp.returncode != 0:
        logging.warning(
            "User doesn't have the Pro Engine installed, not running `semgrep mcp` daemon..."
        )
        pro_engine_available = False
    elif not use_rpc:
        logging.info("USE_SEMGREP_RPC env var is false, not running `semgrep mcp` daemon...")
    elif is_hosted():
        logging.warning(
            """
            The `semgrep mcp` daemon is only available when the MCP server is ran locally.
            User is using the hosted version of the MCP server, not running `semgrep mcp` daemon...
            """
        )
    elif not get_semgrep_app_token():
        logging.warning("No SEMGREP_APP_TOKEN found, not running `semgrep mcp` daemon...")
    else:
        logging.info("Spawning `semgrep mcp` daemon...")
        process = await run_semgrep_process_async(top_level_span, ["mcp", "--pro"])

    return SemgrepContext(
        top_level_span=top_level_span,
        is_hosted=is_hosted(),
        pro_engine_available=pro_engine_available,
        process=process,
        use_rpc=use_rpc,
    )