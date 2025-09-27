# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.request_context
# lines: 13-29
def request_context():
    request_context = MagicMock()
    request_context.session.client_params.clientInfo.name = "fake_cursor"
    request_context.request.headers = {
        "x-oxylabs-username": "oxylabs_username",
        "x-oxylabs-password": "oxylabs_password",
        "x-oxylabs-ai-studio-api-key": "oxylabs_ai_studio_api_key",
    }

    ctx = Context(MagicMock())
    ctx.info = AsyncMock()
    ctx.error = AsyncMock()

    request_ctx.set(request_context)

    with set_context(ctx):
        yield ctx