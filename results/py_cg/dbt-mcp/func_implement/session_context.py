# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/remote_mcp/session.py
# module: src.remote_mcp.session
# qname: src.remote_mcp.session.session_context
# lines: 10-26
async def session_context() -> AsyncGenerator[ClientSession, None]:
    async with (
        streamablehttp_client(
            url=f"https://{os.environ.get('DBT_HOST')}/api/ai/v1/mcp/",
            headers={
                "Authorization": f"token {os.environ.get('DBT_TOKEN')}",
                "x-dbt-prod-environment-id": os.environ.get("DBT_PROD_ENV_ID", ""),
            },
        ) as (
            read_stream,
            write_stream,
            _,
        ),
        ClientSession(read_stream, write_stream) as session,
    ):
        await session.initialize()
        yield session