# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger.warning
# lines: 119-120
    def warning(self, msg: str, **kwargs):
        self._log("WARNING", msg, **kwargs)