# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils._OxylabsClientWrapper.__init__
# lines: 145-150
    def __init__(
        self,
        client: AsyncClient,
    ) -> None:
        self._client = client
        self._ctx = get_context()