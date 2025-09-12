# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger.error
# lines: 122-123
    def error(self, msg: str, **kwargs):
        self._log("ERROR", msg, **kwargs)