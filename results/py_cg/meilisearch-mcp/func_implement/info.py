# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger.info
# lines: 116-117
    def info(self, msg: str, **kwargs):
        self._log("INFO", msg, **kwargs)