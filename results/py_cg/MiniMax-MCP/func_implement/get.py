# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/client.py
# module: minimax_mcp.client
# qname: minimax_mcp.client.MinimaxAPIClient.get
# lines: 89-91
    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a GET request."""
        return self._make_request("GET", endpoint, **kwargs)