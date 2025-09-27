# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.oxylabs_client.wrapper
# lines: 58-62
    async def wrapper(*args, **kwargs):
        client_mock.context_manager_call_args = args
        client_mock.context_manager_call_kwargs = kwargs

        yield client_mock