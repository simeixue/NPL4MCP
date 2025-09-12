# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/server.py
# module: src.meilisearch_mcp.server
# qname: src.meilisearch_mcp.server.MeilisearchMCPServer.__init__
# lines: 36-53
    def __init__(
        self,
        url: str = "http://localhost:7700",
        api_key: Optional[str] = None,
        log_dir: Optional[str] = None,
    ):
        """Initialize MCP server for Meilisearch"""
        # Set up logging directory
        if not log_dir:
            log_dir = os.path.expanduser("~/.meilisearch-mcp/logs")

        self.logger = MCPLogger("meilisearch-mcp", log_dir)
        self.url = url
        self.api_key = api_key
        self.meili_client = MeilisearchClient(url, api_key)
        self.chat_manager = ChatManager(self.meili_client.client)
        self.server = Server("meilisearch")
        self._setup_handlers()