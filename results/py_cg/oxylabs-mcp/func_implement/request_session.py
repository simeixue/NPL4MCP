# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.request_session
# lines: 69-74
def request_session(request_context):
    token = request_ctx.set(request_context)

    yield request_context.session

    request_ctx.reset(token)