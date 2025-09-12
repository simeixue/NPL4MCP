# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/client.py
# module: minimax_mcp.client
# qname: minimax_mcp.client.MinimaxAPIClient.__init__
# lines: 10-23
    def __init__(self, api_key: str, api_host: str):
        """Initialize the API client.
        
        Args:
            api_key: The API key for authentication
            api_host: The API host URL
        """
        self.api_key = api_key
        self.api_host = api_host
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'MM-API-Source': 'Minimax-MCP'
        })