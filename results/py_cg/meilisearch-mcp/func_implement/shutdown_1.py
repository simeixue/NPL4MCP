# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger.shutdown
# lines: 125-128
    def shutdown(self):
        """Clean shutdown of logger"""
        if hasattr(self, "file_handler"):
            self.file_handler.shutdown()