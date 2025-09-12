# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/client.py
# module: src.meilisearch_mcp.client
# qname: src.meilisearch_mcp.client.MeilisearchClient.__init__
# lines: 18-33
    def __init__(
        self, url: str = "http://localhost:7700", api_key: Optional[str] = None
    ):
        """Initialize Meilisearch client"""
        self.url = url
        self.api_key = api_key
        # Add custom user agent to identify this as Meilisearch MCP
        self.client = Client(
            url, api_key, client_agents=("meilisearch-mcp", f"v{__version__}")
        )
        self.indexes = IndexManager(self.client)
        self.documents = DocumentManager(self.client)
        self.settings = SettingsManager(self.client)
        self.tasks = TaskManager(self.client)
        self.keys = KeyManager(self.client)
        self.monitoring = MonitoringManager(self.client)