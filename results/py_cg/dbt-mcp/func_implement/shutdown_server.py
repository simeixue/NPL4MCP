# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/fastapi_app.py
# module: src.dbt_mcp.oauth.fastapi_app
# qname: src.dbt_mcp.oauth.fastapi_app.create_app.shutdown_server
# lines: 192-197
    def shutdown_server() -> dict[str, bool]:
        logger.info("Shutdown server received")
        server = app.state.server_ref
        if server is not None:
            server.should_exit = True
        return {"ok": True}