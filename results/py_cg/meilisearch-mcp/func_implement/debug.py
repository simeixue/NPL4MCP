# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger.debug
# lines: 113-114
    def debug(self, msg: str, **kwargs):
        self._log("DEBUG", msg, **kwargs)