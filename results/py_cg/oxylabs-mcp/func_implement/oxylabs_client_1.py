# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils.oxylabs_client
# lines: 202-228
async def oxylabs_client() -> AsyncIterator[_OxylabsClientWrapper]:
    """Async context manager for Oxylabs client that is used in MCP tools."""
    headers = _get_default_headers()

    username, password = get_oxylabs_auth()

    if not username or not password:
        raise ValueError("Oxylabs username and password must be set.")

    auth = BasicAuth(username=username, password=password)

    async with AsyncClient(
        timeout=Timeout(settings.OXYLABS_REQUEST_TIMEOUT_S),
        verify=True,
        headers=headers,
        auth=auth,
    ) as client:
        try:
            yield _OxylabsClientWrapper(client)
        except HTTPStatusError as e:
            raise MCPServerError(
                f"HTTP error during POST request: {e.response.status_code} - {e.response.text}"
            ) from None
        except RequestError as e:
            raise MCPServerError(f"Request error during POST request: {e}") from None
        except Exception as e:
            raise MCPServerError(f"Error: {str(e) or repr(e)}") from None