# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger.__init__
# lines: 76-78
    def __init__(self, name: str = "meilisearch-mcp", log_dir: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self._setup_logger(log_dir)