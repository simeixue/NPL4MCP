# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.oxylabs_client
# lines: 54-65
def oxylabs_client():
    client_mock = AsyncMock()

    @asynccontextmanager
    async def wrapper(*args, **kwargs):
        client_mock.context_manager_call_args = args
        client_mock.context_manager_call_kwargs = kwargs

        yield client_mock

    with patch("oxylabs_mcp.utils.AsyncClient", new=wrapper):
        yield client_mock