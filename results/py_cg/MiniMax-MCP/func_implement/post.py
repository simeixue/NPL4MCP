# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/client.py
# module: minimax_mcp.client
# qname: minimax_mcp.client.MinimaxAPIClient.post
# lines: 93-95
    def post(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a POST request."""
        return self._make_request("POST", endpoint, **kwargs) 